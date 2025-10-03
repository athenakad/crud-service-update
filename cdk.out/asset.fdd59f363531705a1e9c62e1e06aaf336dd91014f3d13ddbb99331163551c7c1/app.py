from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import os
from influxdb_client import InfluxDBClient, Point
from datetime import datetime, timezone


app = FastAPI()

INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")

def get_client():
    return InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

def get_write_api(client: InfluxDBClient = Depends(get_client)):
    return client.write_api()

def get_query_api(client: InfluxDBClient = Depends(get_client)):
    return client.query_api()

class DataPoint(BaseModel):
    id: str
    value: float

@app.post("/data")
def post_data(point: DataPoint,
              write_api=Depends(get_write_api),
              query_api=Depends(get_query_api)):
    try:
        #check for duplicates
        query = f'''
            from(bucket:"{INFLUXDB_BUCKET}")
            |> range(start:-5m)
            |> filter(fn: (r) => r["_measurement"] == "measurement" and r["id"] == "{point.id}")
            |> limit(n:1)
        '''
        tables = query_api.query(query)

        for table in tables:
            for _ in table.records:
                raise HTTPException(status_code=400, detail=f"Τhe id '{point.id}' already exists.")

        # If it doesn't exist write the new one
        p = Point("measurement").tag("id", point.id).field("value", point.value)
        write_api.write(bucket=INFLUXDB_BUCKET, record=p)
        return {"status": "Data created successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/data")
def get_data(query_api=Depends(get_query_api)):
    try:
        tables = query_api.query(f'from(bucket:"{INFLUXDB_BUCKET}") |> range(start: -1h)')
        results = []
        for table in tables:
            for record in table.records:
                results.append({
                    "time": record.get_time(),
                    "id": record["id"],
                    "value": record["value"]
                })
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/data/{id}")
def put_data(id: str, point: DataPoint, write_api=Depends(get_write_api)):
    try:
        p = Point("measurement").tag("id", id).field("value", point.value)
        write_api.write(bucket=INFLUXDB_BUCKET, record=p)
        return {"status": "updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/data/{id}")
def delete_data(id: str, client: InfluxDBClient = Depends(get_client)):
    try:
        query_api = client.query_api()
        # check if the id exists
        query = f'''
            from(bucket:"{INFLUXDB_BUCKET}")
            |> range(start:-5m)
            |> filter(fn: (r) => r["_measurement"] == "measurement" and r["id"] == "{id}")
            |> limit(n:1)
        '''
        tables = query_api.query(query)
        found = any(True for table in tables for _ in table.records)

        if not found:
            raise HTTPException(status_code=400, detail=f"Τhe id '{id}' doesn't exist.")

        # Delete
        delete_api = client.delete_api()
        delete_api.delete(
            start="1970-01-01T00:00:00Z",
            stop=datetime.now(timezone.utc).isoformat(),
            predicate=f'_measurement="measurement" AND id="{id}"',
            bucket=INFLUXDB_BUCKET,
            org=INFLUXDB_ORG
        )
        return {"status": f"Data {id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

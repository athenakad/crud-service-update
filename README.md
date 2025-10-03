
## Architecture diagram

This project deploys a CRUD API on AWS Fargate behind a public Application Load Balancer (ALB), 
with an InfluxDB database running on a private EC2 instance. 
The ALB receives traffic from the internet and securely routes it to the API containers in private subnets. 
The setup includes auto-scaling, CloudWatch alarms, and SNS notifications for monitoring and high availability.



                                ┌───────────────┐
                                │   Internet    │
                                └──────┬────────┘
                                       │
                               ┌───────▼─────────┐
                               │  ALB (Public)   │
                               │ Load Balancer   │
                               └───────┬─────────┘
                                       │ HTTP:80
                         ┌─────────────▼─────────────┐
                         │ ECS Fargate Service (CRUD)│
                         │ 2 Tasks (Private Subnets) │
                         │ Container: CRUD API       │
                         │ Port: 8080                │
                         └─────────────┬─────────────┘
                                       │ TCP:8086
                         ┌─────────────▼─────────────┐
                         │  InfluxDB EC2 Instance    │
                         │ Private Subnet            │
                         │ t3.micro                  │
                         └─────────────┬─────────────┘
                                       │
                                 VPC Networking
                       ┌───────────────┴───────────────┐
                       │      Public Subnets           │
                       │  NAT Gateway / Internet Access│
                       └───────────────┬───────────────┘
                                       │
                       ┌───────────────▼───────────────┐
                       │     Private Subnets           │
                       │ CRUD API + InfluxDB EC2       │
                       └───────────────────────────────┘


## Local Development
1) Clone and setup environment
```
python -m venv .venv
source .venv/bin/activate
```

2) Install Dependencies
```
pip install -r requirements.txt
```

3) Configure environment variables
Create .env file:
```
INFLUXDB_URL=http://influxdb:8086
INFLUXDB_TOKEN=your-token-here
INFLUXDB_ORG=your-org
INFLUXDB_BUCKET=your-bucket
```

For AWS deployment, update the .env variables to point to your InfluxDB EC2 instance endpoint.

4) Build and Start the Docker Containers
```
docker-compose up --build
```

The API will be available at http://localhost:8080

## AWS Deployment

Prerequisites:

AWS CLI configured
CDK installed: pip install aws-cdk-lib constructs
export .env 


- Validate CDK stack
```
cc
```

- Deploy to AWS
```
cdk deploy
```

- Cleanup
```
cdk destroy
```
## How to Test the Endpoints

You can test the API either via the UI or the CLI. Make sure the Docker container is up and running before testing.


1) Read Data(GET)

Query data with optional parameters such as measurement, start time, and limit:

```
curl -X GET "http://localhost:8080/data"
```

2) Create Data(POST)

Send a POST request to create new data:

```
curl -X POST "http://localhost:8080/data" \
  -H "Content-Type: application/json" \
  -d '{"id":"test","value":42.0}'

```

Expected response:

- To create a new id:
```
Data created successfully
```

- If the id already exists:
```
The {id} already exists
```

3) Update Data (PUT)
```
curl -X PUT "http://localhost:8080/data/sensor1" \
  -H "Content-Type: application/json" \
  -d '{"id":"test","value":55.0}'

```

4) Delete Data(DELETE)

Delete data for a specific measurement:

```
curl -X DELETE "http://localhost:8080/data/test"
```

Expected response:
```
Data deleted successfully
```

- If the id doesn't exist:
```
The {id} doesn't exist
```

5) Run Unit Tests

To run the API unit tests:

```
cd crud_service
pip install httpx
python -m pytest -v test_app.py
```

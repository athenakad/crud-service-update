import unittest
from unittest.mock import MagicMock, Mock, patch
from fastapi.testclient import TestClient
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from app import app


client = TestClient(app)



class TestFastAPIApp(unittest.TestCase):
    @patch('app.InfluxDBClient')
    def test_post_data_success(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        # Mock APIs
        mock_write_api = MagicMock()
        mock_client_instance.write_api.return_value = mock_write_api

        mock_query_api = MagicMock()
        mock_query_api.query.return_value = []
        mock_client_instance.query_api.return_value = mock_query_api

        response = client.post("/data", json={"id": "test", "value": 42.0})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "Data created successfully"})
        self.assertTrue(mock_write_api.write.called)


    @patch('app.InfluxDBClient')
    def test_post_data_duplicate(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        mock_write_api = MagicMock()
        mock_client_instance.write_api.return_value = mock_write_api

        # Duplicate record
        mock_record = MagicMock()
        mock_table = MagicMock()
        mock_table.records = [mock_record]

        mock_query_api = MagicMock()
        mock_query_api.query.return_value = [mock_table]
        mock_client_instance.query_api.return_value = mock_query_api

        response = client.post("/data", json={"id": "duplicate_id", "value": 10.0})

        self.assertEqual(response.status_code, 400)
        self.assertIn("already exists", response.json()["detail"])

    @patch('app.InfluxDBClient')
    def test_get_data(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        mock_record = MagicMock()
        mock_record.get_time.return_value = "2025-10-02T10:00:00Z"
        mock_record.__getitem__ = Mock(side_effect=lambda k: {"id": "test", "value": 42.0}[k])

        mock_table = MagicMock()
        mock_table.records = [mock_record]

        mock_query_api = MagicMock()
        mock_query_api.query.return_value = [mock_table]
        mock_client_instance.query_api.return_value = mock_query_api

        response = client.get("/data")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "results": [{"time": "2025-10-02T10:00:00Z", "id": "test", "value": 42.0}]
        })


    @patch('app.InfluxDBClient')
    def test_put_data(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        mock_write_api = MagicMock()
        mock_client_instance.write_api.return_value = mock_write_api

        response = client.put("/data/test", json={"id": "test", "value": 99.0})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "updated"})
        self.assertTrue(mock_write_api.write.called)


    @patch('app.InfluxDBClient')
    def test_delete_data_success(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        mock_record = MagicMock()
        mock_table = MagicMock()
        mock_table.records = [mock_record]

        mock_query_api = MagicMock()
        mock_query_api.query.return_value = [mock_table]
        mock_client_instance.query_api.return_value = mock_query_api

        mock_delete_api = MagicMock()
        mock_client_instance.delete_api.return_value = mock_delete_api

        response = client.delete("/data/test")

        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted successfully", response.json()["status"])
        self.assertTrue(mock_delete_api.delete.called)


    @patch('app.InfluxDBClient')
    def test_delete_data_not_found(self, mock_influx_client):
        mock_client_instance = MagicMock()
        mock_influx_client.return_value = mock_client_instance

        mock_query_api = MagicMock()
        mock_query_api.query.return_value = []
        mock_client_instance.query_api.return_value = mock_query_api

        response = client.delete("/data/missing_id")

        self.assertEqual(response.status_code, 400)
        self.assertIn("doesn't exist", response.json()["detail"])

if __name__ == "__main__":
    unittest.main()

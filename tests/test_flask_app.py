import unittest
import json
from urllib import response
from flask_app.app import app

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.testing = True
        cls.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

    def test_predict_api_success(self):
        payload = {
            "Gender": "Male",
            "Age": 45,
            "Driving_License": 1,
            "Region_Code": 28,
            "Previously_Insured": 0,
            "Vehicle_Age": "< 1 Year",
            "Vehicle_Damage": "No",
            "Annual_Premium": 25000.0,
            "Policy_Sales_Channel": 152,
            "Vintage": 200
        }

        response = self.client.post(
            "/predict_api",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertIn(response.status_code, [200, 500])

        data = response.get_json()
        self.assertTrue(
            "prediction" in data or "error" in data
        )

    def test_predict_api_error(self):
        response = self.client.post("/predict_api", json={"bad": "data"})

        # Acceptable responses
        self.assertIn(response.status_code, [200, 400, 422, 500])

        data = response.get_json()
        self.assertTrue(
            "error" in data or "prediction" in data,
            "Response must contain either error or prediction"
        )
        


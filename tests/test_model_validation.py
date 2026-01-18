# load test + signature test + performance test

import unittest
import mlflow
import os
import dagshub
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import numpy as np

class TestModelLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up DagsHub credentials for MLflow tracking
        dagshub_token = os.getenv("CAPSTONE_TEST")
        if not dagshub_token:
            raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

        os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
        os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

        dagshub_url = "https://dagshub.com"
        repo_owner = "MANJESH-ctrl"
        repo_name = "MLOPS"

        # Set up MLflow tracking URI
        mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')
        # dagshub.init(repo_owner='MANJESH-ctrl', repo_name='MLOPS', mlflow=True)

          # Load the new model from MLflow model registry
        cls.model_name = "my_model"
        cls.model_version = cls.get_latest_model_version(cls.model_name)
        cls.model_uri = f'models:/{cls.model_name}/{cls.model_version}'
        cls.model = mlflow.pyfunc.load_model(cls.model_uri)

          
        # Load test data
        cls.holdout_data = pd.read_csv("data/processed/test_final.csv")
        cls.x_test = cls.holdout_data.drop("Response", axis=1)
        cls.y_test = cls.holdout_data["Response"]
        print("✅ Setup complete!")

    @staticmethod
    def get_latest_model_version(model_name, stage="None"):
        client = mlflow.MlflowClient()
        latest_version = client.get_latest_versions(model_name, stages=[stage])
        return latest_version[0].version if latest_version else None

    def test_model_loaded_properly(self):
        self.assertIsNotNone(self.__class__.model)

    def test_02_model_signature(self):
        """Test model input/output signature"""
        print("🧪 Test : Model signature...")
        
        # Take a small sample for testing
        sample_size = min(10, len(self.x_test))
        x_sample = self.x_test.iloc[:sample_size]

        # Test prediction
        predictions = self.__class__.model.predict(x_sample)
      
        
        # Check output shapes
        self.assertEqual(len(predictions), sample_size)
        self.assertEqual(predictions.shape[0], sample_size)
        
        # Check predictions are binary (0 or 1)
        self.assertTrue(np.all(np.isin(predictions, [0, 1])))
        
        
        print(f"✅ Signature test passed!")
        print(f"   Sample predictions: {predictions[:1]}")
       


    def test_03_model_performance(self):
        print("🧪 Test : Model performance...")

     

        y_pred = self.__class__.model.predict(self.x_test)

        accuracy_new = accuracy_score(self.y_test, y_pred)
        precision_new = precision_score(self.y_test, y_pred, zero_division=0)
        recall_new = recall_score(self.y_test, y_pred, zero_division=0)
        f1_new = f1_score(self.y_test, y_pred, zero_division=0)
        
        
        # Define expected thresholds for the performance metrics
        expected_accuracy = 0.40
        expected_precision = 0.40
        expected_recall = 0.40
        expected_f1 = 0.40
        
        self.assertGreaterEqual(accuracy_new, expected_accuracy, f'Accuracy should be at least {expected_accuracy}')
        self.assertGreaterEqual(precision_new, expected_precision, f'Precision should be at least {expected_precision}')
        self.assertGreaterEqual(recall_new, expected_recall, f'Recall should be at least {expected_recall}')
        self.assertGreaterEqual(f1_new, expected_f1, f'F1 score should be at least {expected_f1}')


if __name__ == "__main__":
    unittest.main()
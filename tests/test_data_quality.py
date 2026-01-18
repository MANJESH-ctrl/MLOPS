import unittest
import pandas as pd
import numpy as np
import os

class TestDataQuality(unittest.TestCase):
    
    def test_01_train_test_split_consistency(self):
        """Test that train and test data have consistent features"""
        print("🧪 Test: Train-test split consistency...")
        
        train_data = pd.read_csv('data/processed/train_final.csv')
        test_data = pd.read_csv('data/processed/test_final.csv')
        
        # Check same columns
        self.assertEqual(set(train_data.columns), set(test_data.columns))
        
        # Check same feature types
        for col in train_data.columns:
            if col != 'Response':  # Target column
                self.assertEqual(train_data[col].dtype, test_data[col].dtype)
        
        print("✅ Train-test consistency verified!")

    def test_02_no_missing_values(self):
        """Test for missing values in processed data"""
        print("🧪 Test: Missing values check...")
        
        files = ['train_final.csv', 'test_final.csv']
        
        for file in files:
            data = pd.read_csv(f'data/processed/{file}')
            
            # Check for missing values
            missing = data.isnull().sum().sum()
            self.assertEqual(missing, 0, f"Found {missing} missing values in {file}")
            
        print("✅ No missing values found!")

    def test_03_target_distribution(self):
        """Test target variable distribution"""
        print("🧪 Test: Target distribution...")
        
        train_data = pd.read_csv('data/processed/train_final.csv')
        test_data = pd.read_csv('data/processed/test_final.csv')
        
        # Check binary target
        self.assertEqual(set(train_data['Response'].unique()), {0, 1})
        self.assertEqual(set(test_data['Response'].unique()), {0, 1})
        
        # Check no class imbalance is too severe (optional)
        train_ratio = train_data['Response'].mean()
        test_ratio = test_data['Response'].mean()
        
        print(f"   Train positive ratio: {train_ratio:.4f}")
        print(f"   Test positive ratio: {test_ratio:.4f}")
        
        # Ensure both classes are present
        self.assertGreater(train_ratio, 0.05, "Positive class too rare in train")
        self.assertLess(train_ratio, 0.95, "Positive class too common in train")
        
        print("✅ Target distribution is valid!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
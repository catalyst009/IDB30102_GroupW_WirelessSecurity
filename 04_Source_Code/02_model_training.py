from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

def train_lightweight_model(X, y):
    """
    Trains a compact Random Forest classifier suited for TinyML deployment
    on resource-constrained edge devices (ESP32).
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize a lightweight Random Forest (limiting depth and estimators for edge deployment)
    print("Training lightweight Random Forest classifier...")
    clf = RandomForestClassifier(n_estimators=15, max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = clf.predict(X_test)
    
    # Calculate proposed evaluation metrics
    print("\n--- Preliminary Evaluation Metrics ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred, zero_division=0):.4f}")
    
    return clf

if __name__ == "__main__":
    # Generate dummy fused data (representing output from 01_feature_fusion.py)
    np.random.seed(42)
    X_dummy = pd.DataFrame({
        'rssi': np.random.randn(200),
        'csi_amplitude': np.random.randn(200),
        'time_of_arrival_ms': np.random.randn(200)
    })
    y_dummy = np.random.choice([0, 1], 200, p=[0.7, 0.3])
    
    # Train the model
    model = train_lightweight_model(X_dummy, y_dummy)
    print("\nModel ready for TensorFlow Lite Micro conversion.")

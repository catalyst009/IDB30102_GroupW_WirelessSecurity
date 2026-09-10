import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """
    Simulates loading 802.11 management frames captured by the ESP32/SDR.
    Filters out malformed packets and extracts physical-layer features.
    """
    print(f"Loading raw capture data from {filepath}...")
    # In a real scenario, this would read a .csv or parse a .pcap file
    # Creating dummy data to represent the ESP32 capture
    data = {
        'frame_id': range(1, 101),
        'bssid': ['00:14:22:01:23:45'] * 100,
        'rssi': np.random.normal(-65, 5, 100), # Simulating RSSI values
        'csi_amplitude': np.random.normal(12.5, 1.2, 100), # Simulating CSI
        'time_of_arrival_ms': np.linspace(0, 1000, 100), # Simulating ToA
        'label': np.random.choice([0, 1], 100, p=[0.8, 0.2]) # 0 = Legitimate, 1 = Rogue AP
    }
    df = pd.DataFrame(data)
    
    # Drop empty or malformed rows (cleaning)
    df.dropna(inplace=True)
    return df

def fuse_sensors(df):
    """
    Fuses RSSI, CSI amplitude, and ToA into a single feature vector
    as proposed in the Multi-Sensor Feature Fusion Module.
    """
    print("Fusing RSSI, CSI, and ToA into a single feature vector...")
    
    # Selecting the multi-sensor features
    features = df[['rssi', 'csi_amplitude', 'time_of_arrival_ms']]
    labels = df['label']
    
    # Normalizing the features for the TinyML model
    normalized_features = (features - features.mean()) / features.std()
    
    return normalized_features, labels

if __name__ == "__main__":
    # Execute the preprocessing pipeline
    raw_df = load_and_clean_data("sample_esp32_capture.csv")
    X, y = fuse_sensors(raw_df)
    
    print("\nFeature Fusion Complete. Sample of fused vectors:")
    print(X.head())

# Dataset Description: Custom ESP32 Empirical Test-Bed Data

### 1. Data Source
This research utilizes a custom empirical dataset generated using an isolated wireless laboratory test-bed. The data is captured using an ESP32 microcontroller and a Software-Defined Radio (SDR) configured as a capture node. 

### 2. Justification for Custom Dataset
Existing frameworks often rely on static, offline datasets (such as AWID3 or WSN-DS) which fail to capture the real-world environmental dynamics and multipath fading that impact physical-layer security. By generating a custom dataset, this project ensures the evaluation accurately reflects dynamic RF noise and adversarial perturbation vulnerabilities.

### 3. Captured Features
The capture node passively scans 802.11 management frames (beacons and probe responses) to extract the following physical-layer metadata:
* **BSSID:** The MAC address of the broadcasting access point.
* **RSSI (Received Signal Strength Indicator):** Measures the power level being received by the antenna.
* **CSI (Channel State Information):** Captures amplitude and phase variations of the wireless signal.
* **ToA (Time-of-Arrival):** Frame timestamp metadata used for spatial bounding.
* **Label:** Binary classification indicating a Legitimate AP (0) or a Rogue AP/Evil-Twin (1).

### 4. Data Privacy & Ethics
All data collection is strictly confined to a private, isolated test-bed. The capture nodes are configured to extract only physical-layer metadata and MAC headers; they do not log packet payloads or Personally Identifiable Information (PII).

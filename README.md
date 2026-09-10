# DETECTING ROGUE ACCESS POINTS IN EDGE IOT USING MULTI-SENSOR FUSION

### Project Overview
* **Group Number:** Group W
* **Assigned Research Area:** Wireless Security

### Group Members
* NUR ALIYA BINTI MOHD YUSRI (52215125747)
* NUR AMIRAH BINTI ROSLAN (52215125785)
* NUR ALIEYA SOFIA BINTI SAIFULLIZAN (52215125636)
* NUR ALIA MAISARAH BINTI ABD RAHAMAN (52215125613)

---

### 1. Research Problem
Despite advancements in wireless intrusion detection, current security frameworks fail to address two critical operational challenges:
* **Environmental Fragility:** Physical-layer authentication schemes (like RSSI and CSI) exhibit significant performance degradation in real-world deployments due to environmental dynamics and adversarial perturbation attacks.
* **Severe Edge-Deployment Bottlenecks:** Advanced deep neural networks impose massive computational, memory, and energy overheads, causing severe execution latency when deployed on resource-constrained IoT edge endpoints like the ESP32.

### 2. Research Aim
To develop and evaluate a lightweight, environmentally robust wireless security framework that effectively mitigates rogue access points and authentication vulnerabilities without exhausting the computational and energy resources of IoT edge devices.

### 3. Research Objectives
1. To study and systematically analyse existing physical-layer fingerprinting techniques and machine-learning anomaly detection methods used to secure Wi-Fi and BLE networks.
2. To design and develop a lightweight, multi-sensor hybrid security architecture tailored specifically for resource-constrained IoT endpoints, aiming to improve threat detection while minimizing computational overhead.
3. To evaluate the proposed solution's performance in terms of threat detection accuracy, false-positive reduction under dynamic environmental noise, and processing efficiency.

### 4. Brief Description of the Proposed Solution
This research proposes a novel lightweight and multi-sensor approach. Using an ESP32 and Software-Defined Radio (SDR) test-bed, this solution captures and fuses Received Signal Strength Indicator (RSSI), Channel State Information (CSI), and Time-of-Arrival (ToA) meta-data from 802.11 management frames into a single feature vector. This fused vector is then evaluated locally using a quantized TinyML classifier to accurately flag Rogue Access Points (RAP) and Evil-Twins.

### 5. Methodology & Development Model
* **Selected Research Methodology:** Experimental (Quasi-Experimental)
* **Development Model:** Prototyping (evolutionary)

### 6. Proposed Evaluation Plan
* **Baseline:** A conventional single-feature (RSSI-only) threshold detector.
* **Test Environment:** A custom, isolated ESP32/SDR empirical test-bed network containing legitimate APs and a simulated attack node.
* **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, False Positive Rate (FPR), Inference Latency, and Memory Usage.

### 7. Proposed System Architecture
The system is divided into functional layers starting from the edge:
1. **Data Capture Layer:** ESP32/SDR with a Wi-Fi monitor-mode adapter.
2. **Signal Metadata Extractor:** Derives RSSI, CSI, BSSID, and timestamp/ToA.
3. **Multi-Sensor Feature Fusion Module:** Combines the extracted metrics into a single feature vector.
4. **Lightweight On-Device Classifier:** A TinyML model (e.g., Random Forest or compact CNN) that scores anomalies.
5. **Decision Engine & Evaluation Dashboard:** Evaluates the score against thresholds to trigger alerts and log metrics.

### 8. Repository Structure & Technical Components
* `01_Research_Papers/`: Contains reference information for literature reviewed.
* `02_Literature_Review/`: Comparison tables, gap analysis, and identified metrics.
* `03_Architecture_and_Flowchart/`: Proposed system architecture and process flowchart diagrams.
* `04_Source_Code/`: Preliminary Python (data preparation/training) and C++ (TinyML deployment) scripts.
* `05_Data_or_Sample_Input/`: Sample data structures for RSSI, CSI, and ToA metrics.
* `06_Results_or_Expected_Output/`: Evaluation logs format and expected metric outputs.
* `07_References/`: Full APA references and external resources.

### 9. Technology Stack
* **Languages:** Python, C++
* **Hardware:** ESP32 microcontrollers, Software-Defined Radio (SDR), Laptop/PC
* **Frameworks/Tools:** TensorFlow Lite for Microcontrollers (TinyML), TShark
* **Datasets:** Custom empirical dataset generated in an isolated lab test-bed

### 10. Instructions for Executing Preliminary Code
*(Note: Update this section as your `04_Source_Code` folder evolves)*
1. Navigate to the `04_Source_Code/` directory.
2. Run the Python preprocessing scripts to clean the sample raw `.pcap` files.
3. Use the Arduino IDE or PlatformIO to compile and flash the C++ TinyML model to your ESP32 device.

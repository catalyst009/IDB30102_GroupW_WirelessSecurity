# Research Papers and Literature Reviewed

This document outlines the key research papers analyzed for this proposal, adhering to the requirement of not uploading copyrighted PDFs directly to the repository.

---

### 1. DL-PEDR: Deep learning-based phase error distinction and rogue AP detection in wireless IoT
* **Author(s):** Yang, B., Dong, Y., Zhang, W., & Ren, K.
* **Year:** 2024
* **Research Problem:** Rogue Access Point (RAP) Detection
* **Method/Technique:** CSI fingerprinting + Deep Learning
* **Dataset/Tools:** Wireless IoT environments / CSI extraction tools
* **Main Findings:** Achieved a 96.6% RAP detection rate.
* **Limitation:** CSI is highly sensitive to environmental multipath fading.
* **Relevance to Proposed Research:** Highlights the potential of physical-layer features like CSI for authentication, but justifies our decision to fuse CSI with other metrics to overcome its environmental fragility.

---

### 2. Enhancing Wi-Fi network security through stacked machine learning models
* **Author(s):** Winiarski, F., & Natkaniec, M.
* **Year:** 2026
* **Research Problem:** Wireless Intrusion Detection Systems (WIDS)
* **Method/Technique:** Stacked ML (MLP, LightGBM, XGBoost)
* **Dataset/Tools:** AWID3 dataset
* **Main Findings:** Achieved 99.8% accuracy on the AWID3 dataset; reduced false positives.
* **Limitation:** High computational overhead; evaluated offline, limiting edge deployment.
* **Relevance to Proposed Research:** Proves machine learning is highly effective for WIDS, but demonstrates the gap our project aims to fill: the need for lightweight models (TinyML) rather than heavy stacked models that cannot run on edge devices.

---

### 3. Security analysis of WiFi-based sensing systems: Threats from perturbation attacks
* **Author(s):** Cao, H., Huang, W., Xu, G., Chen, X., He, Z., Hu, J., Jiang, H., & Fang, Y.
* **Year:** 2026
* **Research Problem:** Vulnerabilities in Physical-Layer Security (PLS) / Wi-Fi Sensing
* **Method/Technique:** CSI phase extraction & SVD decomposition
* **Dataset/Tools:** WiFi-based sensing systems
* **Main Findings:** Highlights vulnerabilities of RF sensing systems to adversarial noise.
* **Limitation:** Perturbation attacks can degrade classification accuracy by 72.9%.
* **Relevance to Proposed Research:** Directly supports our primary problem statement regarding the "Environmental Fragility" of single-feature PLS methods and justifies our multi-sensor fusion approach.

---

### 4. Machine learning-driven intrusion detection for securing IoT-based wireless sensor networks
* **Author(s):** Munaye, Y. Y., Gebeyehu, A. D., Tai, L.-C., Abebe, Z. A., Workneh, A. B., Tarekegn, R. B., Chekol, Y. B., & Tarekegn, G. B.
* **Year:** 2026
* **Research Problem:** IoT Intrusion Detection
* **Method/Technique:** Machine learning anomaly detection
* **Dataset/Tools:** WSN-DS dataset
* **Main Findings:** High detection rates for IoT sensor networks.
* **Limitation:** Advanced models cause execution latency on constrained hardware.
* **Relevance to Proposed Research:** Reinforces our second problem statement regarding the "Severe Edge-Deployment Bottlenecks" of current ML solutions.

---

### 5. WiFi + Bluetooth scanning, sniffing and predictive analysis of malicious packets using ESP32
* **Author(s):** Kumar, B. S., Ujjainkar, P. A., Yerpude, S., Kaul, S., Qureshi, A., & Ghonge, S.
* **Year:** 2025
* **Research Problem:** Suspicious Behavior Detection at the Edge
* **Method/Technique:** TinyML on ESP32 + Lightweight features
* **Dataset/Tools:** ESP32 microcontrollers
* **Main Findings:** 60% reduction in false alerts.
* **Limitation:** Susceptible to false positives from legitimate background scanning.
* **Relevance to Proposed Research:** Validates our choice of hardware (ESP32) and classification method (TinyML), while showing that using lightweight features alone still leaves room for improvement (false positives) which our fused multi-sensor approach will address.

---

### 6. Smart cyber defense: Machine learning powered intrusion detection in 802.11 networks
* **Author(s):** Kaya, M., Kucukates, H. K., Demez, M., & Kilincer, I. F.
* **Year:** 2024
* **Research Problem:** Attack Classification in 802.11 networks
* **Method/Technique:** K-NN, SVM, and Decision Trees (LightGBM)
* **Dataset/Tools:** 802.11 network captures
* **Main Findings:** Achieved 96.39% accuracy using LightGBM.
* **Limitation:** Reliance on limited frame features caused classification confusion.
* **Relevance to Proposed Research:** Demonstrates that relying on limited data points reduces effectiveness, directly supporting our objective to combine RSSI, CSI, and ToA metadata to improve classification clarity.

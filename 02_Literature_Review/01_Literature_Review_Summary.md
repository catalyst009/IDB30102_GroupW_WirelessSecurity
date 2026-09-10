# Literature Review Summary and Analysis

### 1. Summary of Previous Studies & Comparison of Existing Techniques
| Author(s) & Year | Security Focus | Methodology | Key Findings | Identified Limitations |
| :--- | :--- | :--- | :--- | :--- |
| Yang et al. (2024) | RAP Detection | CSI fingerprinting + Deep Learning | Achieved 96.6% RAP detection rate. | CSI is highly sensitive to environmental multipath fading. |
| Winiarski & Natkaniec (2026) | Wireless IDS | Stacked ML (MLP, LightGBM, XGBoost) | 99.8% accuracy on AWID3 dataset; reduced false positives. | High computational overhead; evaluated offline, limiting edge deployment. |
| Cao et al. (2026) | PLS / Wi-Fi Sensing | CSI phase extraction & SVD decomposition | Highlights vulnerabilities of RF sensing systems to adversarial noise. | Perturbation attacks can degrade classification accuracy by 72.9%. |
| Munaye et al. (2026) | IoT Intrusion Detection | Machine learning on WSN-DS dataset | High detection rates for IoT sensor networks. | Advanced models cause execution latency on constrained hardware. |
| Kumar et al. (2025) | Suspicious Behavior | TinyML on ESP32 + Lightweight features | 60% reduction in false alerts. | Susceptible to false positives from legitimate background scanning. |
| Kaya et al. (2024) | Attack Classification | K-NN, SVM, and Decision Trees | 96.39% accuracy using LightGBM. | Reliance on limited frame features caused classification confusion. |

### 2. Research Gap Analysis
The literature reveals a distinct absence of scalable, distributed, and environmentally robust intrusion mitigation systems tailored for edge microcontrollers. Existing high-accuracy models are too heavy for IoT devices, while lightweight single-feature PLS methods are too fragile in noisy environments (Cao et al., 2026). 

This research directly addresses these gaps by proposing a multi-sensor fusion approach (combining RSSI, CSI, and timing metadata) processed through a lightweight TinyML classifier. This hybrid architecture aims to ensure high detection accuracy and robustness against environmental noise without exhausting the limited resources of IoT endpoints.

### 3. Relevant Datasets & Evaluation Metrics Identified
* **Offline Datasets Used in Previous Work:** AWID3, WSN-DS.
* **Proposed Custom Dataset:** Custom ESP32 empirical test-bed data (to address the gap that offline datasets fail to capture real-world RF dynamics).
* **Identified Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, False Positive Rate (FPR), Inference Latency, and Memory Usage.

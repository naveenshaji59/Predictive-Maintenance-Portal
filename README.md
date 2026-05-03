# ⚙️ Industry 4.0: Predictive Maintenance Portal

## 📌 Project Overview
This project is an interactive, machine learning-powered web application designed to simulate and monitor industrial IoT sensor data. Built with Python and Streamlit, it serves as a prototype for Industry 4.0 predictive maintenance systems. The core machine learning engine utilizes a Random Forest classifier to analyze real-time sensor variables (temperature, vibration, and operation hours) to predict critical machine failures before they occur.

## 🚀 Key Features
* **Live Data Simulation:** Generates and processes synthetic manufacturing sensor data.
* **Predictive Machine Learning Engine:** Implements a `RandomForestClassifier` (achieving 99% accuracy on synthetic data) to classify operational risk.
* **Interactive Dashboard:** A clean, responsive UI built with Streamlit that allows users to manipulate live sensor inputs and instantly view predictive safety alerts.
* **Automated Risk Assessment:** Dynamic logic that flags severe anomalies (e.g., temperatures > 80°C combined with high vibration) for immediate maintenance intervention.

  <img width="1919" height="1079" alt="Screenshot 2026-05-03 131707" src="https://github.com/user-attachments/assets/48001659-f9d6-4d5b-8729-8ae8d07ac5e9" />
<img width="1919" height="1079" alt="Screenshot 2026-05-03 132107" src="https://github.com/user-attachments/assets/8643cae3-5fcb-46b2-a7b8-785dcb48d277" />
<img width="1919" height="1079" alt="Screenshot 2026-05-03 132123" src="https://github.com/user-attachments/assets/4e5df3c4-9467-4201-b4db-1f89a7a12e51" />


## 🛠️ Technical Stack
* **Language:** Python
* **Frontend/Framework:** Streamlit
* **Machine Learning:** scikit-learn
* **Data Manipulation:** pandas, NumPy

## 💻 Installation & Usage
To run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/naveenshaji59/Predictive-Maintenance-Portal.git](https://github.com/naveenshaji59/Predictive-Maintenance-Portal.git)
   cd Predictive-Maintenance-Portal
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## 📈 Future Enhancements
* Integration of a live time-series database (e.g., InfluxDB) for historical trend analysis.
* Implementation of deep learning (LSTM networks) for more complex, time-dependent anomaly detection.
* Deployment to Google Cloud Platform (GCP) or AWS for remote accessibility.

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("⚙️ Industry 4.0: Predictive Maintenance Portal")
st.write("Welcome to the automated sensor monitoring dashboard.")



np.random.seed(42)
data_size = 500


data = pd.DataFrame({
    'Temperature_C': np.random.normal(70, 10, data_size),
    'Vibration_Hz': np.random.normal(50, 5, data_size),
    'Operation_Hours': np.random.uniform(100, 5000, data_size)
})


data['Machine_Failure'] = np.where(
    (data['Temperature_C'] > 80) & (data['Vibration_Hz'] > 55), 1, 0
)


st.subheader("Raw Sensor Data Logging")
st.write("Displaying the first 10 live readings:")
st.dataframe(data.head(10))

st.markdown("---") 
st.subheader("🧠 Machine Learning Engine")


X = data[['Temperature_C', 'Vibration_Hz', 'Operation_Hours']]
y = data['Machine_Failure']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


accuracy = model.score(X_test, y_test)
st.write(f"**Model Status:** Trained successfully with an accuracy of **{accuracy * 100:.2f}%**")



st.sidebar.header("🎛️ Test a Machine")
st.sidebar.write("Adjust the sliders to simulate live sensor data:")


input_temp = st.sidebar.slider("Temperature (°C)", min_value=50.0, max_value=100.0, value=75.0)
input_vib = st.sidebar.slider("Vibration (Hz)", min_value=30.0, max_value=80.0, value=50.0)
input_hours = st.sidebar.number_input("Operation Hours", min_value=100, max_value=5000, value=2000)


user_data = pd.DataFrame([[input_temp, input_vib, input_hours]], 
                         columns=['Temperature_C', 'Vibration_Hz', 'Operation_Hours'])


prediction = model.predict(user_data)


st.subheader("📡 Live Prediction Status")


if prediction[0] == 1:
    st.error("⚠️ WARNING: High Risk of Machine Failure Detected! Immediate maintenance required.")
else:
    st.success("✅ System Nominal: Machine is operating within safe parameters.")
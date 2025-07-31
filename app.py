import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Smart Irrigation System", layout="wide")

# Custom CSS for background
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('background.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .title-text {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    """
    <div class='title-text' style='text-align: center; margin-bottom: 20px;'>
        <h1 style='color:#2c7be5;'>🌱 Smart Irrigation Monitoring System 💧</h1>
        <p style='font-size:18px;'>Control 20-zone sprinkler system based on live sensor input</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load model
try:
    model = joblib.load("Farm_Irrigation_System.pkl")
except Exception as e:
    st.error("Error loading model. Please ensure the file 'Farm_Irrigation_System.pkl' exists and is valid.")
    st.stop()

# Sidebar input
st.sidebar.header("Sensor Input Panel")
sensor_values = []
for i in range(20):
    value = st.sidebar.slider(f"Sensor {i}", 0.0, 1.0, 0.5, 0.01)
    sensor_values.append(value)

# Show current sensor values
cols = st.columns(4)
for i in range(20):
    with cols[i % 4]:
        st.metric(f"Sensor {i}", f"{sensor_values[i]:.2f}")

# Predict button
if st.button("Predict Sprinkler Status"):
    input_data = np.array(sensor_values).reshape(1, -1)

    try:
        prediction = model.predict(input_data)[0]

        st.markdown("### 💡 Prediction Results")
        for i, val in enumerate(prediction):
            st.write(f"Sprinkler for Zone {i}: {'🟢 ON' if val == 1 else '🔴 OFF'}")

        # Plot
        st.markdown("### 📊 Sensor Moisture Profile")
        fig, ax = plt.subplots()
        ax.plot(range(20), sensor_values, marker='o', color='#2c7be5')
        ax.set_xlabel("Sensor Index")
        ax.set_ylabel("Moisture Level")
        ax.set_ylim(0, 1)
        ax.grid(True)
        st.pyplot(fig)

    except ValueError as ve:
        st.error(f"Model input error: {ve}")
    except Exception as ex:
        st.error(f"Prediction error: {ex}")

# Footer
st.markdown("<hr><center>🚀 AICTE Edunet Internship Project | Built using Streamlit</center>", unsafe_allow_html=True)

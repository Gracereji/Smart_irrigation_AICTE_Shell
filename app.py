import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Smart Irrigation System", layout="wide")

# Add a header banner image (optional, hosted online or in your folder)
st.markdown(
    """
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='color:#2c7be5;'>🌱 Smart Irrigation Monitoring System 💧</h1>
        <p style='font-size:18px;'>Simulate and visualize sensor values to manage sprinkler systems</p>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.header("Sensor Input Panel")

# Collecting simulated sensor inputs
moisture = st.sidebar.slider("Soil Moisture (0 - Dry to 1 - Wet)", 0.0, 1.0, 0.4, 0.01)
temperature = st.sidebar.slider("Temperature (°C)", 10, 50, 30)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)

# Display values in columns
col1, col2, col3 = st.columns(3)
col1.metric("🌾 Soil Moisture", f"{moisture:.2f}")
col2.metric("🌡️ Temperature", f"{temperature}°C")
col3.metric("💦 Humidity", f"{humidity}%")

# Dummy prediction logic (you can integrate your ML model here)
def sprinkler_status(moisture, temperature, humidity):
    # Simple logic: if moisture < 0.5 and temperature > 25 and humidity < 70 => Turn ON
    if moisture < 0.5 and temperature > 25 and humidity < 70:
        return "ON"
    else:
        return "OFF"

status = sprinkler_status(moisture, temperature, humidity)

# Display result
st.markdown("### 💡 Sprinkler Status")
if status == "ON":
    st.success("✅ Sprinklers should be turned **ON**")
else:
    st.warning("❌ Sprinklers should remain **OFF**")

# Visual representation
st.markdown("### 📊 Soil Moisture Simulation")
fig, ax = plt.subplots()
x = np.arange(1, 11)
y = np.clip(np.random.normal(moisture, 0.05, size=10), 0, 1)
ax.plot(x, y, marker='o', color='#2c7be5')
ax.set_ylim(0, 1)
ax.set_ylabel("Soil Moisture")
ax.set_xlabel("Sensor Zones")
st.pyplot(fig)

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px;'>🚀 Project created during AICTE Edunet Foundation Internship | Streamlit Powered</p>
    """, unsafe_allow_html=True
)

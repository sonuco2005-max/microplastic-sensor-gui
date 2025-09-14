import streamlit as st
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Microplastic Sensor GUI", layout="wide")

st.title("🌊 Microplastic Sensor - GUI Mockup")

# Mode selection
mode = st.radio("Select Mode:", ["LED Mode", "Microscope Mode"])

# ----------------- LED MODE -----------------
if mode == "LED Mode":
    st.subheader("LED Mode Controls")
    
    wavelengths = [370, 385, 395, 405, 456, 470, 525, 570, 590, 605, 625, 636, 840, 940]
    selected_wl = st.multiselect("Select Wavelengths (nm):", wavelengths)
    
    led_power = st.slider("LED Power (%)", 0, 100, 80)
    samples = st.selectbox("Samples to Run:", [1, 2, 3])
    
    st.write(f"Selected wavelengths: {selected_wl}")
    st.write(f"LED Power: {led_power}%")
    st.write(f"Samples: {samples}")

    # Simulated scanning
    if st.button("Start Scan"):
        progress = st.progress(0)
        data = []
        for i in range(100):
            v = 1.65 + 0.5*np.sin(time.time()*2) + 0.1*np.random.randn()
            v = max(0.0, min(3.3, v))  # clamp 0–3.3V
            data.append(v)
            progress.progress(i+1)
            time.sleep(0.05)

        st.success("Scan Complete ✅")
        df = pd.DataFrame({"Index": list(range(len(data))), "Voltage (V)": data})
        st.line_chart(df.set_index("Index"))

# ----------------- MICROSCOPE MODE -----------------
else:
    st.subheader("Microscope Mode Controls")
    x_pos = st.number_input("Motor X Position", value=0.0, step=0.5)
    y_pos = st.number_input("Motor Y Position", value=0.0, step=0.5)

    if st.button("Move Motors"):
        st.info(f"Motors moved to X={x_pos}, Y={y_pos}")

    if st.button("Snap Image"):
        st.image("https://via.placeholder.com/640x480.png?text=Microscope+Image", caption="Simulated Snapshot")

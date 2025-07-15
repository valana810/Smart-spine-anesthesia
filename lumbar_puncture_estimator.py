import streamlit as st

# Title
st.title("🧠 Smart Lumbar Puncture Point Estimator")

# Intro
st.markdown("""
This tool estimates the optimal lumbar puncture sites (L2–L3, L3–L4, L4–L5) based on anatomical proportions and 
provides a recommended spinal anesthesia dose using basic patient metrics.
""")

# Sidebar: Patient Info
st.sidebar.header("👤 Patient Information")
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=0)
gender = st.sidebar.selectbox("Gender", ["Select", "Male", "Female", "Other"])
height = st.sidebar.number_input("Height (cm)", min_value=0, max_value=250, value=0)
weight = st.sidebar.number_input("Weight (kg)", min_value=0, max_value=200, value=0)

# Main Input
neck_to_hip = st.number_input("Enter Neck to Hip Distance (cm):", min_value=0.0, max_value=120.0, value=0.0)

# Lumbar Level Estimation
def estimate_lumbar_positions(neck_hip_cm):
    l2_l3_pos = round(neck_hip_cm * (1 - 0.64), 1)
    l3_l4_pos = round(neck_hip_cm * (1 - 0.68), 1)
    l4_l5_pos = round(neck_hip_cm * (1 - 0.72), 1)
    return l2_l3_pos, l3_l4_pos, l4_l5_pos

# Dose Estimation
def calculate_dose(weight, age, height):
    base_dose = 1.2
    weight_factor = 0.02
    age_factor = 0.01
    height_factor = 0.005
    return round(base_dose + (weight * weight_factor) + (age * age_factor) + (height * height_factor), 2)

# Output
if neck_to_hip > 0 and height > 0 and weight > 0 and age > 0 and gender != "Select":
    l2_l3, l3_l4, l4_l5 = estimate_lumbar_positions(neck_to_hip)
    dose = calculate_dose(weight, age, height)

    st.subheader("📍 Estimated Lumbar Puncture Points (from Hip Upwards):")
    st.success(f"🔸 L2–L3: *{l2_l3} cm* from hip")
    st.success(f"🔸 L3–L4: *{l3_l4} cm* from hip")
    st.success(f"🔸 L4–L5: *{l4_l5} cm* from hip")

    st.subheader("💉 Recommended Spinal Anesthesia Dose:")
    st.info(f"Estimated dose: *{dose} mL* (based on age, height, weight)")
else:
    st.warning("Please fill in all patient details to get accurate results.")
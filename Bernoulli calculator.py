import streamlit as st
import math

# Constants
g = 9.81
rho = 1000  # Density of water in kg/m^3

st.title("Bernoulli Equation Calculator")
st.write("Calculate pressure, velocity, and elevation heads using the Bernoulli principle.")

# Sidebar for navigation
choice = st.sidebar.radio(
    "Select Calculation:",
    (
        "1. Calculate Pressure Head",
        "2. Calculate Velocity Head",
        "3. Calculate Elevation Head",
        "4. Calculate Unknown Pressure (P2)",
        "5. Calculate Unknown Velocity (V2)"
    )
)

st.header(choice)

if choice == "1. Calculate Pressure Head":
    P = st.number_input("Enter pressure (Pa):", value=0.0, step=100.0)
    if st.button("Calculate"):
        pressure_head = P / (rho * g)
        st.success(f"**Pressure Head = {pressure_head:.4f} m**")

elif choice == "2. Calculate Velocity Head":
    V = st.number_input("Enter velocity (m/s):", value=0.0, step=0.5)
    if st.button("Calculate"):
        velocity_head = (V**2) / (2 * g)
        st.success(f"**Velocity Head = {velocity_head:.4f} m**")

elif choice == "3. Calculate Elevation Head":
    z = st.number_input("Enter elevation (m):", value=0.0, step=0.5)
    if st.button("Calculate"):
        st.success(f"**Elevation Head = {z:.4f} m**")

elif choice == "4. Calculate Unknown Pressure (P2)":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Point 1")
        P1 = st.number_input("Pressure at point 1 (Pa):", value=0.0, step=100.0)
        V1 = st.number_input("Velocity at point 1 (m/s):", value=0.0, step=0.5)
        z1 = st.number_input("Elevation at point 1 (m):", value=0.0, step=0.5)
    with col2:
        st.subheader("Point 2")
        V2 = st.number_input("Velocity at point 2 (m/s):", value=0.0, step=0.5)
        z2 = st.number_input("Elevation at point 2 (m):", value=0.0, step=0.5)

    if st.button("Calculate Pressure P2"):
        # Fixed formula: P2 = P1 + 0.5*rho*(V1^2 - V2^2) + rho*g*(z1 - z2)
        P2 = P1 + (0.5 * rho * (V1**2 - V2**2)) + (rho * g * (z1 - z2))
        st.success(f"**Unknown Pressure (P2) = {P2:.2f} Pa**")

elif choice == "5. Calculate Unknown Velocity (V2)":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Point 1")
        P1 = st.number_input("Pressure at point 1 (Pa):", value=0.0, step=100.0)
        V1 = st.number_input("Velocity at point 1 (m/s):", value=0.0, step=0.5)
        z1 = st.number_input("Elevation at point 1 (m):", value=0.0, step=0.5)
    with col2:
        st.subheader("Point 2")
        P2 = st.number_input("Pressure at point 2 (Pa):", value=0.0, step=100.0)
        z2 = st.number_input("Elevation at point 2 (m):", value=0.0, step=0.5)

    if st.button("Calculate Velocity V2"):
        V2_squared = V1**2 + (2 * (P1 - P2) / rho) + (2 * g * (z1 - z2))

        if V2_squared >= 0:
            V2 = math.sqrt(V2_squared)
            st.success(f"**Unknown Velocity (V2) = {V2:.4f} m/s**")
        else:
            st.error("No real velocity is possible with these inputs (Negative square root).")

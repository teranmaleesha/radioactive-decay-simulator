import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Radioactive Decay Simulator",
    page_icon="⚛️",
    layout="wide"
)

# Title and Introduction
st.title("⚛️ Radioactive Decay & Isotope Half-Life Simulation Dashboard")
st.markdown("""
This interactive web application simulates the radioactive decay of various isotopes over time
based on their half-lives. Designed for educational, scientific research, and portfolio demonstration purposes.
""")

# Sidebar Configuration
st.sidebar.header("⚙️ Simulation Parameters")

isotope_choice = st.sidebar.selectbox(
    "Select Isotope:",
    ["Carbon-14 (C-14)", "Uranium-235 (U-235)", "Cobalt-60 (Co-60)", "Custom"]
)

# Define Half-Lives
if isotope_choice == "Carbon-14 (C-14)":
    half_life = 5730
    unit = "Years"
elif isotope_choice == "Uranium-235 (U-235)":
    half_life = 704000000
    unit = "Years"
elif isotope_choice == "Cobalt-60 (Co-60)":
    half_life = 5.27
    unit = "Years"
else:
    half_life = st.sidebar.number_input("Custom Half-life:", min_value=1.0, value=10.0)
    unit = "Units"

initial_atoms = st.sidebar.slider("Initial Number of Atoms ($N_0$):", min_value=1000, max_value=100000, value=10000, step=1000)
max_time_multiplier = st.sidebar.slider("Number of Half-lives to Simulate:", min_value=1, max_value=10, value=5)

max_time = half_life * max_time_multiplier
time = np.linspace(0, max_time, 500)

# Decay Formula: N(t) = N_0 * e^(-decay_constant * t)
decay_constant = np.log(2) / half_life
remaining_atoms = initial_atoms * np.exp(-decay_constant * time)

# Layout: Two Columns (Graph on left, Metrics on right)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📈 Decay Curve for {isotope_choice}")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(time, remaining_atoms, color='#ff4b4b', linewidth=2.5, label='Remaining Atoms')
    ax.set_xlabel(f'Time ({unit})', fontsize=12)
    ax.set_ylabel('Remaining Atoms ($N$)', fontsize=12)
    ax.set_title(f'Radioactive Decay (Half-life = {half_life:,.2f} {unit})', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("📊 Summary Statistics")
    st.metric(label="Selected Isotope", value=isotope_choice)
    st.metric(label="Half-Life", value=f"{half_life:,.2f} {unit}")
    st.metric(label="Initial Atoms ($N_0$)", value=f"{initial_atoms:,}")

    final_atoms = initial_atoms * (0.5 ** max_time_multiplier)
    st.metric(label="Final Remaining Atoms", value=f"{int(final_atoms):,}")

st.markdown("---")
st.markdown("🚀 *Developed by J.D. Teran Maleesha | Advanced Scientific Programming Portfolio*")

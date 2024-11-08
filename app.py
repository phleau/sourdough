import streamlit as st

def bereken_watertemperatuur(omgeving_en_meel_temp, gewenste_deeg_temp, frictie_factor):
    return 3 * gewenste_deeg_temp - omgeving_en_meel_temp * 2 - frictie_factor

# Concise title
st.title("Water Temp Guide")

# Friendly, engaging description with emojis
st.markdown("<h4>💧 Calculate the perfect water temp for your dough!<br> (Assuming room and flour temps match)</h4>", unsafe_allow_html=True)

# Input fields with clear labels and logical order
omgeving_en_meel_temp = st.number_input("🌡️ Room & Flour Temperature (°C)", min_value=-20, max_value=50, value=20)
gewenste_deeg_temp = st.number_input("🍞 Desired Dough Temperature (°C)", min_value=-20, max_value=50, value=25)
methode = st.radio("👩‍🍳 Mixing Method", ('Hand', 'Machine'))
frictie_factor = 1 if methode == 'Hand' else 7

# Calculate button with improved label
if st.button("Get Water Temp 💧"):
    watertemperatuur = bereken_watertemperatuur(omgeving_en_meel_temp, gewenste_deeg_temp, frictie_factor)
    st.success(f"🥄 The water temperature should be: **{watertemperatuur:.2f}°C**")

# Personal note
st.markdown("<br><sub>Created with ❤️ by Flo</sub>", unsafe_allow_html=True)

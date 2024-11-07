import streamlit as st

def bereken_watertemperatuur(omgeving_temp, meel_temp, gewenste_deeg_temp):
    return 3 * gewenste_deeg_temp - omgeving_temp - meel_temp

st.title("Watertemperatuur Calculator voor Zuurdesem")
st.write("Vul de gegevens in om de optimale watertemperatuur voor je zuurdesemstarter te berekenen.")

omgeving_temp = st.number_input("Omgevingstemperatuur (°C)", min_value=-20, max_value=50, value=20)
meel_temp = st.number_input("Meeltemperatuur (°C)", min_value=-20, max_value=50, value=22)
gewenste_deeg_temp = st.number_input("Gewenste Deegtemperatuur (°C)", min_value=-20, max_value=50, value=25)

if st.button("Bereken Watertemperatuur"):
    watertemperatuur = bereken_watertemperatuur(omgeving_temp, meel_temp, gewenste_deeg_temp)
    st.success(f"De benodigde watertemperatuur is: {watertemperatuur:.2f}°C")

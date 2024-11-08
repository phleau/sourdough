import streamlit as st

def bereken_watertemperatuur(omgeving_en_meel_temp, gewenste_deeg_temp, frictie_factor):
    return 3 * gewenste_deeg_temp - omgeving_en_meel_temp * 2 - frictie_factor

st.title("What temperature should the water be?")
st.write("When making sourdough bread, you can use this calculator to determine the optimal temperature for your water.")
st.write("Assuming the room and flour temperature are the same:")

# Eén inputveld voor zowel kamertemperatuur als meeltemperatuur
omgeving_en_meel_temp = st.number_input("Room and flour temperature (°C)", min_value=-20, max_value=50, value=20)
gewenste_deeg_temp = st.number_input("Desirable dough temperature (°C)", min_value=-20, max_value=50, value=25)

# Keuze voor frictiefactor (handmatig of machine)
methode = st.radio("Mixing method", ('Hand', 'Machine'))
frictie_factor = 1 if methode == 'Hand' else 7

if st.button("Calculate!"):
    watertemperatuur = bereken_watertemperatuur(omgeving_en_meel_temp, gewenste_deeg_temp, frictie_factor)
    st.success(f"The water should be: {watertemperatuur:.2f}°C")

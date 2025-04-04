import streamlit as st

st.title("Checkbox + Number Test")

want_bread = st.checkbox("Sourdough bread")
if want_bread:
    quantity_bread = st.number_input("How many loaves?", min_value=1, max_value=2, step=1)
    st.write(f"You selected {quantity_bread} sourdough loaves.")

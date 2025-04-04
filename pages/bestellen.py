import streamlit as st

st.set_page_config(page_title="Bestellen", page_icon="📝")

st.title("Bestellen")

with st.form("order_form"):
    name = st.text_input("Naam")
    
    item = st.selectbox(
        "Wat wil je bestellen?",
        ["Brood", "Croissant", "Brioche", "Pain au chocolat"]
    )
    
    quantity = st.number_input("Aantal", min_value=1, max_value=100, step=1)

    submitted = st.form_submit_button("Verstuur bestelling")

    if submitted:
        st.success(f"Bedankt {name}! Je hebt {quantity} x {item} besteld.")

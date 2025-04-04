import streamlit as st

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

with st.form("order_form"):
    name = st.text_input("Your name")

    st.markdown("### What would you like to order?")
    
    order = {}

    # Sourdough bread
    want_bread = st.checkbox("Sourdough bread")
    if want_bread:
        quantity_bread = st.number_input("Number of loaves (max 2)", min_value=1, max_value=2, step=1, key="bread")
        order["Sourdough bread"] = quantity_bread

    # Croissant
    want_croissant = st.checkbox("Croissant")
    if want_croissant:
        quantity_croissant = st.number_input("Number of croissants (max 3)", min_value=1, max_value=3, step=1, key="croissant")
        order["Croissant"] = quantity_croissant

    # Brioche
    want_brioche = st.checkbox("Brioche")
    if want_brioche:
        quantity_brioche = st.number_input("Number of brioches (max 2)", min_value=1, max_value=2, step=1, key="brioche")
        order["Brioche"] = quantity_brioche

    submitted = st.form_submit_button("Submit order")

    if submitted:
        if not name:
            st.error("Please enter your name.")
        elif not order:
            st.error("Please select at least one item to order.")
        else:
            st.success(f"Thank you, {name}! Your order has been submitted.")
            for item, qty in order.items():
                st.write(f"- {qty} x {item}")

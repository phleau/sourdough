import streamlit as st

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# Ask for name first
name = st.text_input("Your name")

if name:
    with st.form("order_form"):
        st.markdown("### What would you like to order?")
        
        order = {}

        # Sourdough bread
        want_bread = st.checkbox("Sourdough bread", key="want_bread")
        if want_bread:
            quantity_bread = st.number_input("Number of loaves (max 2)", min_value=1, max_value=2, step=1, key="qty_bread")
            order["Sourdough bread"] = quantity_bread

        # Croissant
        want_croissant = st.checkbox("Croissant", key="want_croissant")
        if want_croissant:
            quantity_croissant = st.number_input("Number of croissants (max 3)", min_value=1, max_value=3, step=1, key="qty_croissant")
            order["Croissant"] = quantity_croissant

        # Brioche
        want_brioche = st.checkbox("Brioche", key="want_brioche")
        if want_brioche:
            quantity_brioche = st.number_input("Number of brioches (max 2)", min_value=1, max_value=2, step=1, key="qty_brioche")
            order["Brioche"] = quantity_brioche

        submitted = st.form_submit_button("Submit order")

        if submitted:
            if not order:
                st.error("Please select at least one item to order.")
            else:
                st.success(f"Thank you, {name}! Your order has been submitted.")
                for item, qty in order.items():
                    st.write(f"- {qty} x {item}")
else:
    st.info("Please enter your name to begin your order.")

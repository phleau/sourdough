import streamlit as st

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# Ask for name first
name = st.text_input("Your name")

if name:
    with st.form("order_form"):
        st.markdown("### What would you like to order?")
        
        order = {}

        st.markdown("**Sourdough bread**")
        quantity_bread = st.selectbox(
            "Number of loaves", options=[0, 1, 2], index=0, key="qty_bread"
        )
        if quantity_bread > 0:
            order["Sourdough bread"] = quantity_bread

        st.markdown("**Croissant**")
        quantity_croissant = st.selectbox(
            "Number of croissants", options=[0, 1, 2, 3], index=0, key="qty_croissant"
        )
        if quantity_croissant > 0:
            order["Croissant"] = quantity_croissant

        st.markdown("**Brioche**")
        quantity_brioche = st.selectbox(
            "Number of brioches", options=[0, 1, 2], index=0, key="qty_brioche"
        )
        if quantity_brioche > 0:
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

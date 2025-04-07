import streamlit as st
import json
import requests

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# 🔽 Replace with your actual GitHub raw file URL
PRODUCTS_URL = "https://raw.githubusercontent.com/phleau/sourdough/main/data/products.json"

try:
    response = requests.get(PRODUCTS_URL)
    response.raise_for_status()
    products = response.json()
except Exception as e:
    st.error("Could not load product list. Please try again later.")
    st.stop()

name = st.text_input("Your name")

if name:
    with st.form("order_form"):
        st.markdown("### What would you like to order?")
        order = {}

        for product_name, max_qty in products.items():
            st.markdown(f"**{product_name}**")
            quantity = st.selectbox(
                f"Number of {product_name.lower()}s",
                options=list(range(0, max_qty + 1)),
                index=0,
                key=f"qty_{product_name}"
            )
            if quantity > 0:
                order[product_name] = quantity

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

import streamlit as st
import json
import requests

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# 🔽 Load products.json from GitHub
PRODUCTS_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/data/products.json"

try:
    response = requests.get(PRODUCTS_URL)
    response.raise_for_status()
    products = response.json()
except Exception as e:
    st.error("Could not load product list. Please try again later.")
    st.stop()

# 👤 Ask for name first
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
                key=f"

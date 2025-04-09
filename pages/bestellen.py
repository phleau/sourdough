import streamlit as st
import json
import requests
import pandas as pd

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# 🔽 Replace with your actual GitHub raw file URL
PRODUCTS_URL = "https://raw.githubusercontent.com/phleau/sourdough/main/data/products.json"
GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyxM-cSYgKyKtn0iOVhVa8JFWS2QwfWSnf9MsKIRGEmS1VGAqd-y5BDTK4EXa8bkIDv/exec"


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
            order[product_name] = quantity

        submitted = st.form_submit_button("Submit order")

        if submitted:
            st.success(f"Thank you, {name}! Your order has been submitted.")
            for item, qty in order.items():
            st.write(f"- {qty} x {item}")

        # 🔄 Send data to Google Sheet
            payload = {
            "name": name,
            **order
        }
    
        try:
            r = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
            if r.status_code == 200:
                st.info("Your order was saved.")
            else:
                st.warning("Could not confirm if order was saved.")
        except Exception as e:
            st.error(f"Failed to send order to Google Sheet: {e}")
else:
    st.info("Please enter your name to begin your order.")

st.markdown("---")
st.markdown("## 🧾 Recent Orders")

ORDERS_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTKavwizrwv2x7OTaMWZXprZuabNQIXtuod3nMAnYPRUP4DewfR89Jw-Tv-9kYUNd0TvaRaWnRqWHbe/pubhtml?gid=0&single=true"

def load_orders():
    try:
        df = pd.read_csv(ORDERS_CSV_URL)
        return df
    except Exception as e:
        st.error("Could not load order data.")
        return None

df_orders = load_orders()
if df_orders is not None:
    st.dataframe(df_orders.tail(10))  # Show the last 10 orders

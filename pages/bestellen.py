import streamlit as st
import json
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

# URLs
PRODUCTS_URL = "https://raw.githubusercontent.com/phleau/sourdough/main/data/products.json"
GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyxM-cSYgKyKtn0iOVhVa8JFWS2QwfWSnf9MsKIRGEmS1VGAqd-y5BDTK4EXa8bkIDv/exec"
ORDERS_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTKavwizrwv2x7OTaMWZXprZuabNQIXtuod3nMAnYPRUP4DewfR89Jw-Tv-9kYUNd0TvaRaWnRqWHbe/pub?gid=0&single=true&output=csv"

# Load product list
try:
    response = requests.get(PRODUCTS_URL)
    response.raise_for_status()
    product_config = response.json()
    product_names = list(product_config.keys())
except Exception as e:
    st.error("Could not load product list. Please try again later.")
    st.stop()

# Load previous orders
@st.cache_data(ttl=60)
def load_orders():
    try:
        df = pd.read_csv(ORDERS_CSV_URL)
        return df
    except Exception:
        return None

df_orders = load_orders()

# Compute already ordered quantities
total_ordered = {product: 0 for product in product_names}
if df_orders is not None and not df_orders.empty:
    for product in product_names:
        if product in df_orders.columns:
            total_ordered[product] = df_orders[product].fillna(0).astype(int).sum()

# Order form
name = st.text_input("Your name")

if name:
    with st.form("order_form"):
        st.markdown("### What would you like to order?")
        order = {}

        for product_name in product_names:
            config = product_config[product_name]
            max_per_person = config.get("per_person", 10)
            max_total = config.get("total_available")
            already_ordered = total_ordered.get(product_name, 0)

            if max_total is not None:
                remaining_stock = max(0, max_total - already_ordered)
                max_available = min(max_per_person, remaining_stock)
            else:
                max_available = max_per_person

            if max_total is not None:
                st.caption(f"{remaining_stock} remaining out of {max_total}")

            quantity = st.selectbox(
                product_name,
                options=list(range(0, max_available + 1)),
                index=0,
                key=f"qty_{product_name}"
            )
            order[product_name] = quantity

        submitted = st.form_submit_button("Submit order")

        if submitted:
            st.success(f"Thank you, {name}! Your order has been submitted.")
            for item, qty in order.items():
                st.write(f"- {qty} x {item}")

            payload = {
                "name": name,
                **order
            }

            try:
                r = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
                if r.status_code == 200:
                    st.info("Your order was saved.")
                    st.cache_data.clear()
                    df_orders = load_orders()
                else:
                    st.warning("Could not confirm if order was saved.")
            except Exception as e:
                st.error(f"Failed to send order to Google Sheet: {e}")
else:
    st.info("Please enter your name to begin your order.")

# Show recent orders
st.markdown("---")
st.markdown("## 🗏️ Recent Orders")

if df_orders is not None and not df_orders.empty:
    st.dataframe(df_orders.tail(10).iloc[::-1])
else:
    st.info("No orders yet. Be the first to place one!")

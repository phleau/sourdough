import streamlit as st
import json
import requests
import pandas as pd

st.set_page_config(page_title="Order", page_icon="📝")
st.title("Place your order")

st.markdown("""
**This Saturday 17th of May, another session! You're welcome between 10h30–12h30**

- 🍓 Brioche bun with baked matcha crème pâtissière & strawberry–rhubarb compote — **3.5€**  
  _Ingredients:_ *flour, plant-based butter, eggs, plant-based milk, sourdough starter, yeast, sugar, salt, matcha, cornstarch, rhubarb, strawberries*

- 🌿 Lemon, capers & salsa verde sourdough focaccia — **4€** (max 27 pieces)  
  _Ingredients:_ *wheat flour, water, sourdough starter, olive oil, salt, lemon peel, capers, coriander, parsley, dill*

- 🌾 Fig fennel scone — **3.5€**  
  _Ingredients:_ *flour, plant-based butter, dried figs (non-colonized origin), sugar, salt, plant-based milk, baking powder, fennel seed*

- 🍞 Spelt sesame sourdough (800g) — **4€** (max 18)  
  _Ingredients:_ *organic Graanbroeders wholespelt flour, wheat flour, water, sourdough starter, sesame seeds, salt*

- 🥖 Bonus: some extra baguettes if Flo manages ;)

All ingredients are organic
""")


# URLs
PRODUCTS_URL = "https://raw.githubusercontent.com/phleau/sourdough/main/data/products.json"
GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyxM-cSYgKyKtn0iOVhVa8JFWS2QwfWSnf9MsKIRGEmS1VGAqd-y5BDTK4EXa8bkIDv/exec"
ORDERS_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTKavwizrwv2x7OTaMWZXprZuabNQIXtuod3nMAnYPRUP4DewfR89Jw-Tv-9kYUNd0TvaRaWnRqWHbe/pub?gid=0&single=true&output=csv"

# Load product list
try:
    response = requests.get(PRODUCTS_URL)
    response.raise_for_status()
    products = response.json()
except Exception as e:
    st.error("Could not load product list. Please try again later.")
    st.stop()

# Order form
name = st.text_input("Your name")

if name:
    with st.form("order_form"):
        st.markdown("### What would you like to order?")
        order = {}

        for product_name, max_qty in products.items():
            quantity = st.selectbox(
                product_name,
                options=list(range(0, max_qty + 1)),
                index=0,
                key=f"qty_{product_name}"
            )
            order[product_name] = quantity

        submitted = st.form_submit_button("Submit order", disabled = True)

        if submitted:
            st.success(f"Thank you, {name}! Your order has been submitted.")
            st.cache_data.clear()
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
                else:
                    st.warning("Could not confirm if order was saved.")
            except Exception as e:
                st.error(f"Failed to send order to Google Sheet: {e}")
else:
    st.info("Please enter your name to begin your order.")

# Show recent orders
st.markdown("---")
st.subheader("📋 Recent Orders")

@st.cache_data(ttl=10)
def load_orders():
    try:
        df = pd.read_csv(ORDERS_CSV_URL)
        return df
    except Exception:
        return None

df_orders = load_orders()
if df_orders is not None and not df_orders.empty:
    st.dataframe(df_orders.iloc[::-1])
else:
    st.info("No orders yet. Be the first to place one!")

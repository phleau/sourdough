import streamlit as st
st.set_page_config(page_title="Redirecting...", layout="wide", initial_sidebar_state="collapsed")

if "redirected" not in st.session_state:
    st.session_state.redirected = True
    st.switch_page("Bake Studio Flo")

st.write("Redirecting...")


import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import os
from cricbuzz_client import CricbuzzClient
from init_database import init_db

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")
st.title("⚙️ System Diagnostics & Settings")

st.subheader("API Connectivity Test")
client = CricbuzzClient()
if st.button("Test Cricbuzz RapidAPI Connection"):
    success, msg = client.test_connection()
    if success:
        st.success(f"Connection OK! {msg}")
    else:
        st.warning(f"Notice: {msg} (Application running in offline mock/database mode)")

st.markdown("---")
st.subheader("Database Maintenance")
if st.button("Reset Database to Seed State"):
    init_db()
    st.success("Database restored to seed state with schema and tables!")

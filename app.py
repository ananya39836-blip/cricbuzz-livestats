import streamlit as st
import pandas as pd
from connection import get_connection

st.set_page_config(page_title="Cricbuzz LiveStats", page_icon="🏏", layout="wide")

st.title("🏏 Cricbuzz LiveStats Dashboard")
st.markdown("**Real-Time Cricket Insights & SQL-Based Analytics**")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

try:
    conn = get_connection()
    p_count = pd.read_sql("SELECT COUNT(*) AS c FROM players;", conn)["c"][0]
    m_count = pd.read_sql("SELECT COUNT(*) AS c FROM matches;", conn)["c"][0]
    t_count = pd.read_sql("SELECT COUNT(*) AS c FROM teams;", conn)["c"][0]
    v_count = pd.read_sql("SELECT COUNT(*) AS c FROM venues;", conn)["c"][0]
    conn.close()
except Exception:
    p_count, m_count, t_count, v_count = 0, 0, 0, 0

col1.metric("Total Players", p_count)
col2.metric("Total Matches", m_count)
col3.metric("Teams Registered", t_count)
col4.metric("Venues Tracked", v_count)

st.markdown("---")
st.subheader("📌 Project Navigation & System Modules")
st.markdown("""
Use the **sidebar menu** to access all modules:
- **1_Live_Matches:** Real-time matches, live scorecards, and commentary feeds.
- **2_Top_Stats:** Batting and bowling leaderboards visualised via charts.
- **3_SQL_Analytics:** All 25 analytical SQL questions with results and query executor.
- **4_CRUD_Operations:** Manage cricket database records (Create, Read, Update, Delete).
- **5_Settings:** API connection diagnostics, venue data import, and database resets.
""")

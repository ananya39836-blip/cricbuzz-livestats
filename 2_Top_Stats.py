import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) if os.path.dirname(__file__) else ".")
import streamlit as st
import pandas as pd
from connection import get_connection
from charts import create_bar_chart

st.set_page_config(page_title="Top Stats", page_icon="📊", layout="wide")
st.title("📊 Player Leaderboards & Top Stats")

format_choice = st.selectbox("Select Cricket Format", ["ODI", "Test", "T20I"])

conn = get_connection()
df_batting = pd.read_sql(f"""
    SELECT p.full_name, pcs.runs_scored, pcs.batting_average, pcs.strike_rate, pcs.centuries
    FROM player_career_stats pcs
    JOIN players p ON pcs.player_id = p.player_id
    WHERE pcs.format = '{format_choice}'
    ORDER BY pcs.runs_scored DESC LIMIT 10;
""", conn)

c1, c2 = st.columns(2)
with c1:
    st.subheader(f"Top Run Scorers ({format_choice})")
    st.dataframe(df_batting, use_container_width=True)

with c2:
    if not df_batting.empty:
        fig = create_bar_chart(df_batting, "full_name", "runs_scored", f"Highest Run Scorers ({format_choice})")
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
df_bowling = pd.read_sql(f"""
    SELECT p.full_name, pcs.wickets_taken, pcs.bowling_average, pcs.economy_rate
    FROM player_career_stats pcs
    JOIN players p ON pcs.player_id = p.player_id
    WHERE pcs.format = '{format_choice}' AND pcs.wickets_taken > 0
    ORDER BY pcs.wickets_taken DESC LIMIT 10;
""", conn)
conn.close()

c3, c4 = st.columns(2)
with c3:
    st.subheader(f"Top Wicket Takers ({format_choice})")
    st.dataframe(df_bowling, use_container_width=True)

with c4:
    if not df_bowling.empty:
        fig_bowl = create_bar_chart(df_bowling, "full_name", "wickets_taken", f"Most Wickets ({format_choice})")
        st.plotly_chart(fig_bowl, use_container_width=True)

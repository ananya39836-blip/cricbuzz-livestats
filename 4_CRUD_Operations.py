import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import pandas as pd
from repositories import get_all_players, add_player, update_player, delete_player, get_all_teams

st.set_page_config(page_title="CRUD Operations", page_icon="✏️", layout="wide")
st.title("✏️ Player Database Management (CRUD)")

tab1, tab2, tab3 = st.tabs(["View Players", "Add Player", "Edit / Delete Player"])

teams_df = get_all_teams()
team_dict = dict(zip(teams_df["team_name"], teams_df["team_id"]))

with tab1:
    st.subheader("Current Players List")
    players_df = get_all_players()
    st.dataframe(players_df, use_container_width=True)

with tab2:
    st.subheader("Register New Player")
    with st.form("add_player_form"):
        name = st.text_input("Full Name")
        team = st.selectbox("Team", list(team_dict.keys()))
        role = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
        bat = st.selectbox("Batting Style", ["Right-hand bat", "Left-hand bat"])
        bowl = st.selectbox("Bowling Style", ["Right-arm fast", "Right-arm offbreak", "Slow left-arm orthodox", "None"])
        
        submitted = st.form_submit_button("Add Player")
        if submitted:
            if name.strip():
                add_player(name, team_dict[team], role, bat, bowl)
                st.success(f"Player '{name}' added successfully!")
                st.rerun()
            else:
                st.error("Player name cannot be empty.")

with tab3:
    st.subheader("Modify Player Details")
    if not players_df.empty:
        p_names = dict(zip(players_df["full_name"], players_df["player_id"]))
        sel_name = st.selectbox("Select Player", list(p_names.keys()))
        sel_id = p_names[sel_name]
        
        row = players_df[players_df["player_id"] == sel_id].iloc[0]
        with st.form("edit_player_form"):
            new_name = st.text_input("Name", value=row["full_name"])
            new_role = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"], index=["Batsman", "Bowler", "All-rounder", "Wicket-keeper"].index(row["playing_role"]) if row["playing_role"] in ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"] else 0)
            new_bat = st.text_input("Batting Style", value=row["batting_style"] or "Right-hand bat")
            new_bowl = st.text_input("Bowling Style", value=row["bowling_style"] or "Right-arm fast")
            
            c1, c2 = st.columns(2)
            update_btn = c1.form_submit_button("Update Player")
            delete_btn = c2.form_submit_button("Delete Player")
            
            if update_btn:
                update_player(sel_id, new_name, new_role, new_bat, new_bowl)
                st.success("Player updated successfully!")
                st.rerun()
            if delete_btn:
                delete_player(sel_id)
                st.warning(f"Player '{new_name}' deleted!")
                st.rerun()

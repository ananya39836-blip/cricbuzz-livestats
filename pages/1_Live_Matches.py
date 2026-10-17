import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from cricbuzz_client import CricbuzzClient

st.set_page_config(page_title="Live Matches", page_icon="🔴", layout="wide")
st.title("🔴 Live Cricket Matches")

client = CricbuzzClient()
data = client.get_live_matches()

matches_found = []
for type_match in data.get("typeMatches", []):
    m_type = type_match.get("matchType", "Match")
    for series in type_match.get("seriesMatches", []):
        s_wrapper = series.get("seriesAdWrapper", {})
        s_name = s_wrapper.get("seriesName", "Tournament")
        for match in s_wrapper.get("matches", []):
            info = match.get("matchInfo", {})
            score = match.get("matchScore", {})
            matches_found.append({"type": m_type, "series": s_name, "info": info, "score": score})

if matches_found:
    for m in matches_found:
        info = m["info"]
        score = m["score"]
        t1 = info.get("team1", {}).get("teamName", "Team 1")
        t2 = info.get("team2", {}).get("teamName", "Team 2")
        status = info.get("status", "Live")
        venue = info.get("venueInfo", {}).get("ground", "Ground")
        
        with st.container():
            st.subheader(f"{t1} vs {t2}")
            st.caption(f"Series: {m['series']} | Venue: {venue}")
            st.info(f"Status: **{status}**")
            
            s1 = score.get("team1Score", {}).get("inngs1", {})
            s2 = score.get("team2Score", {}).get("inngs1", {})
            if s1 or s2:
                c1, c2 = st.columns(2)
                if s1:
                    c1.metric(t1, f"{s1.get('runs', 0)}/{s1.get('wickets', 0)} ({s1.get('overs', 0)} ov)")
                if s2:
                    c2.metric(t2, f"{s2.get('runs', 0)}/{s2.get('wickets', 0)} ({s2.get('overs', 0)} ov)")
            st.markdown("---")
else:
    st.warning("No ongoing live fixtures found.")

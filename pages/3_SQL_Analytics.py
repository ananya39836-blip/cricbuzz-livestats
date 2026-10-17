import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) if os.path.dirname(__file__) else ".")
import streamlit as st
import pandas as pd
from connection import get_connection

st.set_page_config(page_title="SQL Analytics", page_icon="⚡", layout="wide")
st.title("⚡ 25 SQL Analytical Queries")

question_list = [f"Question {i+1}" for i in range(25)]
selected_q = st.selectbox("Choose Question to Inspect", question_list)
q_num = selected_q.split()[1].zfill(2)

# Check both possible locations for queries (in sql/queries/ or root/queries or flat)
q_file = f"sql/queries/q{q_num}.sql"
if not os.path.exists(q_file):
    q_file = f"q{q_num}.sql"

if os.path.exists(q_file):
    with open(q_file, "r", encoding="utf-8") as f:
        sql_content = f.read()
    
    st.markdown(f"### Query: {selected_q}")
    st.code(sql_content, language="sql")
    
    try:
        conn = get_connection()
        df_res = pd.read_sql(sql_content, conn)
        conn.close()
        st.dataframe(df_res, use_container_width=True)
        
        csv = df_res.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results CSV", data=csv, file_name=f"query_{q_num}_results.csv", mime="text/csv")
    except Exception as e:
        st.error(f"Error executing query: {e}")

st.markdown("---")
st.subheader("🔍 Custom Read-Only SQL Console")
user_query = st.text_area("Type your SELECT query:", "SELECT * FROM teams LIMIT 5;")
if st.button("Run Query"):
    if not user_query.strip().upper().startswith(("SELECT", "WITH")):
        st.warning("Only read-only SELECT or WITH queries are permitted here.")
    else:
        try:
            conn = get_connection()
            custom_df = pd.read_sql(user_query, conn)
            conn.close()
            st.dataframe(custom_df, use_container_width=True)
        except Exception as err:
            st.error(f"Execution Error: {err}")

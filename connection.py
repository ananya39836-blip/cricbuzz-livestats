import os
import sqlite3
import math

os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

DB_PATH = "data/cricket.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.create_function("SQRT", 1, math.sqrt)
    return conn

# For backwards compatibility with pd.read_sql(..., engine)
engine = DB_PATH

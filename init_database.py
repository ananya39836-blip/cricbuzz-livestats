import os
import sqlite3
import math

DB_PATH = "data/cricket.db"
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.create_function("SQRT", 1, math.sqrt)
    
    scripts = ["sql/schema.sql", "sql/indexes.sql", "sql/views.sql", "sql/seed.sql"]
    for s in scripts:
        if os.path.exists(s):
            with open(s, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
            print(f"Executed: {s}")
    conn.commit()
    conn.close()
    print("Database initialized successfully at data/cricket.db")

if __name__ == "__main__":
    init_db()

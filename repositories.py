import pandas as pd
import sqlite3
from connection import get_connection

def get_all_players():
    conn = get_connection()
    query = """
        SELECT p.player_id, p.full_name, t.team_name, p.playing_role, p.batting_style, p.bowling_style
        FROM players p LEFT JOIN teams t ON p.team_id = t.team_id
        ORDER BY p.full_name ASC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def add_player(full_name, team_id, role, bat_style, bowl_style):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO players (full_name, team_id, playing_role, batting_style, bowling_style)
        VALUES (?, ?, ?, ?, ?);
        """,
        (full_name, team_id, role, bat_style, bowl_style)
    )
    conn.commit()
    conn.close()

def update_player(player_id, full_name, role, bat_style, bowl_style):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE players 
        SET full_name = ?, playing_role = ?, batting_style = ?, bowling_style = ?
        WHERE player_id = ?;
        """,
        (full_name, role, bat_style, bowl_style, player_id)
    )
    conn.commit()
    conn.close()

def delete_player(player_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM players WHERE player_id = ?;", (player_id,))
    conn.commit()
    conn.close()

def get_all_teams():
    conn = get_connection()
    df = pd.read_sql("SELECT team_id, team_name FROM teams ORDER BY team_name;", conn)
    conn.close()
    return df

def get_all_matches():
    conn = get_connection()
    query = """
        SELECT m.match_id, m.match_description, t1.team_name AS team1, t2.team_name AS team2, 
               v.venue_name, m.match_date, m.format, tw.team_name AS winner
        FROM matches m
        JOIN teams t1 ON m.team1_id = t1.team_id
        JOIN teams t2 ON m.team2_id = t2.team_id
        JOIN venues v ON m.venue_id = v.venue_id
        LEFT JOIN teams tw ON m.winner_id = tw.team_id
        ORDER BY m.match_date DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

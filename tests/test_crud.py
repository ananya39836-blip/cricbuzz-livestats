import pytest
import sqlite3
import pandas as pd
from connection import get_connection
from repositories import get_all_players, add_player, delete_player

def test_database_connection():
    assert get_connection() is not None

def test_get_players():
    df = get_all_players()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 0

def test_add_and_delete_player():
    add_player("Test Player", 1, "Batsman", "Right-hand bat", "None")
    df = get_all_players()
    assert "Test Player" in df["full_name"].values
    
    p_id = df[df["full_name"] == "Test Player"]["player_id"].values[0]
    delete_player(p_id)
    df_after = get_all_players()
    assert "Test Player" not in df_after["full_name"].values

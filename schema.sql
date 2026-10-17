PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    short_name TEXT
);

CREATE TABLE IF NOT EXISTS venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    capacity INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS series (
    series_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_name TEXT NOT NULL,
    host_country TEXT NOT NULL,
    match_type TEXT NOT NULL,
    start_date DATE NOT NULL,
    total_matches INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    team_id INTEGER,
    playing_role TEXT CHECK(playing_role IN ('Batsman', 'Bowler', 'All-rounder', 'Wicket-keeper')),
    batting_style TEXT,
    bowling_style TEXT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS player_career_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    format TEXT CHECK(format IN ('Test', 'ODI', 'T20I')),
    matches_played INTEGER DEFAULT 0,
    runs_scored INTEGER DEFAULT 0,
    batting_average REAL DEFAULT 0.0,
    strike_rate REAL DEFAULT 0.0,
    centuries INTEGER DEFAULT 0,
    wickets_taken INTEGER DEFAULT 0,
    bowling_average REAL DEFAULT 0.0,
    economy_rate REAL DEFAULT 0.0,
    catches INTEGER DEFAULT 0,
    stumpings INTEGER DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    UNIQUE(player_id, format)
);

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id INTEGER,
    match_description TEXT NOT NULL,
    team1_id INTEGER NOT NULL,
    team2_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    match_date DATE NOT NULL,
    format TEXT CHECK(format IN ('Test', 'ODI', 'T20I')),
    winner_id INTEGER,
    victory_margin INTEGER,
    victory_type TEXT CHECK(victory_type IN ('runs', 'wickets', 'tie', 'no result')),
    toss_winner_id INTEGER,
    toss_decision TEXT CHECK(toss_decision IN ('bat', 'bowl')),
    is_completed BOOLEAN DEFAULT 1,
    FOREIGN KEY (series_id) REFERENCES series(series_id),
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id),
    FOREIGN KEY (winner_id) REFERENCES teams(team_id),
    FOREIGN KEY (toss_winner_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS innings (
    innings_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    innings_number INTEGER NOT NULL,
    batting_team_id INTEGER NOT NULL,
    total_runs INTEGER DEFAULT 0,
    wickets INTEGER DEFAULT 0,
    overs REAL DEFAULT 0.0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (batting_team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS batting_performances (
    perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    innings_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    batting_position INTEGER NOT NULL,
    runs_scored INTEGER DEFAULT 0,
    balls_faced INTEGER DEFAULT 0,
    fours INTEGER DEFAULT 0,
    sixes INTEGER DEFAULT 0,
    strike_rate REAL DEFAULT 0.0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (innings_id) REFERENCES innings(innings_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS bowling_performances (
    bowl_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    innings_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    overs_bowled REAL DEFAULT 0.0,
    runs_conceded INTEGER DEFAULT 0,
    wickets_taken INTEGER DEFAULT 0,
    economy_rate REAL DEFAULT 0.0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (innings_id) REFERENCES innings(innings_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

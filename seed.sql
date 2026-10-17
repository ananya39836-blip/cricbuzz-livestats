INSERT OR IGNORE INTO teams (team_id, team_name, country, short_name) VALUES
(1, 'India', 'India', 'IND'),
(2, 'Australia', 'Australia', 'AUS'),
(3, 'England', 'England', 'ENG'),
(4, 'South Africa', 'South Africa', 'SA');

INSERT OR IGNORE INTO venues (venue_id, venue_name, city, country, capacity) VALUES
(1, 'Narendra Modi Stadium', 'Ahmedabad', 'India', 132000),
(2, 'Melbourne Cricket Ground', 'Melbourne', 'Australia', 100024),
(3, 'Eden Gardens', 'Kolkata', 'India', 68000),
(4, 'Lord''s Cricket Ground', 'London', 'England', 31100),
(5, 'Wankhede Stadium', 'Mumbai', 'India', 33108);

INSERT OR IGNORE INTO series (series_id, series_name, host_country, match_type, start_date, total_matches) VALUES
(1, 'India tour of Australia 2024', 'Australia', 'Test', '2024-11-22', 5),
(2, 'ICC Men''s T20 World Cup 2024', 'USA & West Indies', 'T20I', '2024-06-01', 55),
(3, 'England tour of India 2024', 'India', 'Test', '2024-01-25', 5);

INSERT OR IGNORE INTO players (player_id, full_name, team_id, playing_role, batting_style, bowling_style) VALUES
(1, 'Virat Kohli', 1, 'Batsman', 'Right-hand bat', 'Right-arm medium'),
(2, 'Rohit Sharma', 1, 'Batsman', 'Right-hand bat', 'Right-arm offbreak'),
(3, 'Jasprit Bumrah', 1, 'Bowler', 'Right-hand bat', 'Right-arm fast'),
(4, 'Ravindra Jadeja', 1, 'All-rounder', 'Left-hand bat', 'Slow left-arm orthodox'),
(5, 'Pat Cummins', 2, 'Bowler', 'Right-hand bat', 'Right-arm fast'),
(6, 'Glenn Maxwell', 2, 'All-rounder', 'Right-hand bat', 'Right-arm offbreak'),
(7, 'Joe Root', 3, 'Batsman', 'Right-hand bat', 'Right-arm offbreak'),
(8, 'Ben Stokes', 3, 'All-rounder', 'Left-hand bat', 'Right-arm fast-medium');

INSERT OR IGNORE INTO player_career_stats (player_id, format, matches_played, runs_scored, batting_average, strike_rate, centuries, wickets_taken, bowling_average, economy_rate, catches, stumpings) VALUES
(1, 'ODI', 295, 13906, 58.18, 93.5, 50, 5, 166.2, 6.2, 152, 0),
(1, 'Test', 113, 8848, 49.15, 55.5, 29, 0, 0.0, 0.0, 111, 0),
(1, 'T20I', 125, 4188, 48.69, 137.04, 1, 4, 51.0, 8.05, 54, 0),
(2, 'ODI', 265, 10866, 49.16, 92.4, 31, 9, 64.3, 5.2, 93, 0),
(3, 'ODI', 89, 79, 7.9, 48.2, 0, 149, 24.3, 4.6, 25, 0),
(3, 'Test', 36, 212, 6.2, 35.1, 0, 159, 20.69, 2.76, 12, 0),
(4, 'ODI', 197, 2756, 32.42, 85.2, 0, 220, 36.1, 4.88, 73, 0),
(4, 'Test', 72, 3034, 36.11, 58.2, 4, 294, 24.1, 2.45, 43, 0),
(5, 'ODI', 88, 452, 13.7, 72.1, 0, 141, 28.1, 5.23, 30, 0),
(6, 'ODI', 142, 3934, 35.44, 126.8, 4, 74, 49.2, 5.58, 88, 0),
(7, 'Test', 143, 12000, 50.2, 56.4, 32, 60, 44.5, 3.1, 190, 0),
(8, 'Test', 105, 6350, 35.8, 59.2, 13, 201, 32.1, 3.3, 105, 0);

INSERT OR IGNORE INTO matches (match_id, series_id, match_description, team1_id, team2_id, venue_id, match_date, format, winner_id, victory_margin, victory_type, toss_winner_id, toss_decision, is_completed) VALUES
(1, 2, 'India vs Australia T20I Final', 1, 2, 1, '2024-06-29', 'T20I', 1, 24, 'runs', 2, 'bowl', 1),
(2, 3, 'India vs England 1st Test', 1, 3, 3, '2024-01-25', 'Test', 3, 28, 'runs', 3, 'bat', 1),
(3, 1, 'Australia vs India 1st Test', 2, 1, 2, '2024-11-22', 'Test', 1, 295, 'runs', 1, 'bat', 1),
(4, 2, 'India vs South Africa Final', 1, 4, 5, '2024-06-29', 'T20I', 1, 7, 'runs', 1, 'bat', 1);

INSERT OR IGNORE INTO innings (innings_id, match_id, innings_number, batting_team_id, total_runs, wickets, overs) VALUES
(1, 1, 1, 1, 205, 5, 20.0),
(2, 1, 2, 2, 181, 7, 20.0),
(3, 4, 1, 1, 176, 7, 20.0),
(4, 4, 2, 4, 169, 8, 20.0);

INSERT OR IGNORE INTO batting_performances (match_id, innings_id, player_id, batting_position, runs_scored, balls_faced, fours, sixes, strike_rate) VALUES
(1, 1, 2, 1, 92, 41, 7, 8, 224.39),
(1, 1, 1, 2, 0, 5, 0, 0, 0.0),
(4, 3, 1, 1, 76, 59, 6, 2, 128.81),
(4, 3, 4, 6, 9, 2, 0, 1, 450.0);

INSERT OR IGNORE INTO bowling_performances (match_id, innings_id, player_id, overs_bowled, runs_conceded, wickets_taken, economy_rate) VALUES
(1, 2, 3, 4.0, 24, 2, 6.0),
(1, 2, 4, 4.0, 32, 1, 8.0),
(4, 4, 3, 4.0, 18, 2, 4.5);
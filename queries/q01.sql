-- Q1: Find all players who represent India
SELECT p.full_name, p.playing_role, p.batting_style, p.bowling_style FROM players p JOIN teams t ON p.team_id = t.team_id WHERE t.team_name = 'India';
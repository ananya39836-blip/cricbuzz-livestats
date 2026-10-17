CREATE VIEW IF NOT EXISTS v_match_results AS
SELECT 
    m.match_id,
    m.match_description,
    t1.team_name AS team1,
    t2.team_name AS team2,
    tw.team_name AS winner,
    m.victory_margin,
    m.victory_type,
    v.venue_name,
    v.city,
    m.match_date,
    m.format
FROM matches m
JOIN teams t1 ON m.team1_id = t1.team_id
JOIN teams t2 ON m.team2_id = t2.team_id
LEFT JOIN teams tw ON m.winner_id = tw.team_id
JOIN venues v ON m.venue_id = v.venue_id;

CREATE VIEW IF NOT EXISTS v_team_wins AS
SELECT 
    t.team_name,
    COUNT(m.match_id) AS total_wins
FROM teams t
LEFT JOIN matches m ON t.team_id = m.winner_id
GROUP BY t.team_id, t.team_name
ORDER BY total_wins DESC;

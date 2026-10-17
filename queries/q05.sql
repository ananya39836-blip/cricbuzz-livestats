-- Q5: Total match wins per team
SELECT t.team_name, COUNT(m.match_id) AS total_wins FROM teams t JOIN matches m ON t.team_id = m.winner_id GROUP BY t.team_id, t.team_name ORDER BY total_wins DESC;
SELECT 
    player_id,
    min(event_date) AS "first_login"
FROM Activity a
GROUP BY player_id

-- runtime: 480ms, beats 73.76%
-- memory: 0.00MB, beats 100.00% 
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS "Rank"
FROM Scores;

-- runtime: 232ms, beats 24.04%
-- memory: 0.00MB, beats 100%   
SELECT 
    p.lastName,
    p.firstName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON a.personID = p.personID

-- runtime: 250ms, beats 50.63%
-- memory: 0.00MB, beats 100% 
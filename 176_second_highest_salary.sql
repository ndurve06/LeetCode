SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    --LIMIT 1 OFFSET 1
) AS "SecondHighestSalary";

-- runtime: 202ms, beats 53.69%
-- memory: 0.00MB, beats 100% 
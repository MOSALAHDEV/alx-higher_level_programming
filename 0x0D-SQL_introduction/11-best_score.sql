-- Retrieve records from second_table ordered by score, where score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

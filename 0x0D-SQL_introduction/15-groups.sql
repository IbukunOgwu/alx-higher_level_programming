--Lists the number of recors with the same score in the second_table in MySQL server.
--Records are ordered in descending order
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;

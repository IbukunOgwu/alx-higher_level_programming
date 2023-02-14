--Lists all records in the second_table with a score >= 10 in MySQL server.
--Records are ordered in descending order

SELECT 'score', 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;

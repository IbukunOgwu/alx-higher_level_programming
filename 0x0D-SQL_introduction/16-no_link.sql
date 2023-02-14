--Lists all records of second_table having a name value in MySQL server
--Records are ordered in descending order
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' != ""
ORDER BY 'score' DESC;

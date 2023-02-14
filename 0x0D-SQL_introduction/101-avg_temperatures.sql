--Displays the average temperature (in Farenheit) by city ordered in descending temperature.
SELECT 'city', AVG('value') AS 'avg_temp'
FROM 'temperatures'
GROUP BY 'city'
ORDER BY 'avg_temp' DESC;

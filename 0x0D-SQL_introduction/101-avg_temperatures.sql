-- show the city and average tempreature attributes from temp table
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
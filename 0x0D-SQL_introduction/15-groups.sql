-- show scoure and number of elements holding the same score 
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
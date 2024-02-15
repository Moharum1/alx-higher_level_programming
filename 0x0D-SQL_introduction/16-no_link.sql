-- show score and name for any element with a non empty name attribute
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL  ORDER BY score DESC;
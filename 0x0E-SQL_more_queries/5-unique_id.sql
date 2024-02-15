-- Create a table with non null values in SQL
CREATE TABLE IF NOT EXISTS unique_id 
    (id INT DEFAULT 1, UNIQUE(ID), name VARCHAR(256));
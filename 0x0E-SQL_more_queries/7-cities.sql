-- create a db with an auto generated id primary key
    -- forgin key which is the state id 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
    (
        id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
        state_id INT UNIQUE,
        FOREIGN KEY(state_id) REFERENCES states(id),
        name VARCHAR(256) NOT NULL
    )
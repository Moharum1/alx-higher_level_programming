-- Create a user and give it Select permission on a certin db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* to 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
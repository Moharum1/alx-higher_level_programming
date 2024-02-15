-- Create a User on Sql SERVER and give it all permissions
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
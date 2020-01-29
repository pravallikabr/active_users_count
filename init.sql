CREATE DATABASE IF NOT EXISTS test_db;
CREATE DATABASE IF NOT EXISTS presentation_db;

CREATE USER 'newuser'@'%' IDENTIFIED BY 'newpassword';
GRANT ALL PRIVILEGES ON test_db.* to 'newuser'@'%'  WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON presentation_db.* TO 'newuser'@'%' WITH GRANT OPTION;
CREATE TABLE test_db.users (
    event_date int,
    user_count int );
CREATE TABLE presentation_db.users (
    event_date int not null primary key,
    user_count int );
FLUSH PRIVILEGES;

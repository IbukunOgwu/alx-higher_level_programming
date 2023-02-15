-- Creates the table hbtn_0d_usa and table States on the MySQL server
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
-- Use a database
USE hbtn_0d_usa;
-- Creates the table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));

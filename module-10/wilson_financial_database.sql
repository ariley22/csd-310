/*
    Title: Wilson_Financial_Database.sql
    Author: Jaci Brown, Amanda Riley, Gabriel Sanchez-Jorgensen, Hlee Xiong
    Date: 2/22/24
    Description: Wilson Financial Database Initialization Script
*/

CREATE DATABASE wilson_financial;
USE wilson_financial;

-- drop database user if exists 
DROP USER IF EXISTS 'wilson_user'@'localhost';

-- create wilson_user and grant them all privileges to the wilson_financial database 
CREATE USER 'wilson_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'money';

-- grant all privileges to the wilson_financial database to user wilson_user on localhost 
GRANT ALL PRIVILEGES ON wilson_financial.* TO 'wilson_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS transactions;

-- creating clients table

CREATE TABLE clients (
  client_id INT NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(45) NOT NULL,
  l_name VARCHAR(45) NOT NULL,
  date_added DATE NOT NULL,
  PRIMARY KEY (client_id));

-- creating accounts table

CREATE TABLE accounts (
account_id INT NOT NULL AUTO_INCREMENT,
client_id INT NOT NULL,
account_type ENUM('low-risk', 'high-risk', 'retirement'),
PRIMARY KEY (account_id),
INDEX client_id_idx (client_id ASC),
CONSTRAINT client_id
  FOREIGN KEY (client_id)
  REFERENCES clients (client_id));

ALTER TABLE accounts AUTO_INCREMENT=100;

-- creating transactions table

CREATE TABLE transactions (
  trans_id INT NOT NULL AUTO_INCREMENT,
  client_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  amount INT NOT NULL,
  account_id INT NOT NULL,
  PRIMARY KEY (trans_id),
  INDEX t_client_id_idx (client_id ASC),
  CONSTRAINT t_client_id
    FOREIGN KEY (client_id)
    REFERENCES clients (client_id),
  INDEX account_id (account_id ASC),
  CONSTRAINT account_id
    FOREIGN KEY (account_id)
    REFERENCES accounts (account_id));

  ALTER TABLE transactions AUTO_INCREMENT=1000;

-- populating clients table

INSERT INTO clients
(f_name, l_name, date_added)
VALUES 
('Bob', 'Sanchez', '2023-03-09'),
('Alice', 'Johnson', '2023-04-15'),
('Carlos', 'Diaz', '2023-05-22'),
('Emily', 'Brighton', '2023-06-05'),
('David', 'Smith', '2023-12-01'),
('Elena', 'Martinez', '2024-01-02');


-- populating accounts table. Two clients have two accounts, the rest have 1

INSERT INTO accounts
(client_id, account_type)
VALUES
(1, 'high-risk'),
(1, 'low-risk'),
(2, 'high-risk'),
(3, 'low-risk'),
(4, 'high-risk'),
(4, 'low-risk'),
(5, 'retirement'),
(6, 'retirement');

-- populating transactions table

INSERT INTO transactions
(client_id, transaction_date, amount, account_id)
VALUES
(1,'2023-03-09',3000,100),
(1,'2023-04-15',3000,101),
(2,'2023-05-22',6000,102),
(3,'2023-06-05',1200,103),
(4,'2023-12-01',2500,104),
(4,'2024-01-02',2500,105),
(5,'2023-12-01',300,106),
(5,'2023-12-04',300,106),
(5,'2023-12-07',300,106),
(5,'2023-12-10',300,106),
(5,'2023-12-13',300,106),
(5,'2023-12-16',300,106),
(5,'2023-12-19',300,106),
(5,'2023-12-22',300,106),
(5,'2023-12-25',300,106),
(5,'2023-12-28',300,106),
(5,'2023-12-30',300,106),
(5,'2024-01-01',300,106),
(5,'2024-01-04',300,106),
(5,'2024-01-07',300,106),
(5,'2024-01-10',300,106),
(5,'2024-01-13',300,106),
(5,'2024-01-16',300,106),
(5,'2024-01-19',300,106),
(5,'2024-01-22',300,106),
(5,'2024-01-25',300,106),
(5,'2024-01-28',300,106),
(5,'2024-01-31',300,106),
(5,'2024-02-01',300,106),
(5,'2024-02-04',300,106),
(5,'2024-02-04',300,106),
(5,'2024-02-07',300,106),
(5,'2024-02-10',300,106),
(5,'2024-02-13',300,106),
(5,'2024-02-16',300,106),
(5,'2024-02-19',300,106),
(5,'2024-02-03',300,106),
(5,'2024-02-08',300,106),
(6,'2024-01-02',300,107),
(6,'2024-01-05',300,107),
(6,'2024-01-08',300,107),
(6,'2024-01-11',300,107),
(6,'2024-01-14',300,107),
(6,'2024-01-17',300,107),
(6,'2024-01-20',300,107),
(6,'2024-01-23',300,107),
(6,'2024-01-26',300,107),
(6,'2024-01-29',300,107),
(6,'2024-02-01',300,107),
(6,'2024-02-04',300,107),
(6,'2024-02-07',300,107),
(6,'2024-02-10',300,107),
(6,'2024-02-13',300,107),
(6,'2024-02-16',300,107),
(6,'2024-02-19',300,107),
(6,'2024-02-18',300,107),
(6,'2024-02-17',300,107),
(6,'2024-02-02',300,107);
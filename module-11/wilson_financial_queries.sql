/*
    Group 9: Jaci Brown, Amanda Riley, Gabriel Sanchez-Jorgensen, Hlee Xiong
    Date: 2/29/24
*/

-- DISPLAYING CILENTS ADDED FOR PAST SIX MONTHS --
select concat(f_name, ' ', l_name) as 'Client_Name', monthname(date_added) as 'Month_Added'
from clients 
where date_added >= '2023-09-01' AND date_added < '2024-03-01';

-- DISPLAYING AVERAGE AMOUNT OF ASSETS FOR ALL CLIENTS--
SELECT FORMAT(AVG(total_assets), 2) AS average_assets
FROM (
    SELECT c.client_id, SUM(t.amount) AS total_assets
    FROM clients c
    LEFT JOIN transactions t ON c.client_id = t.client_id
    GROUP BY c.client_id
) AS client_assets;

-- DISPLAYING ALL CLIENTS WITH HIGH NUMBER OF TRANSACTIONS--
SELECT CONCAT(c.f_name, ' ', c.l_name) AS Client_Name,
       COUNT(t.trans_id) AS monthly_transaction_count,
       MONTH(t.transaction_date) AS transaction_month,
       YEAR(t.transaction_date) AS transaction_year
FROM clients c
LEFT JOIN transactions t ON t.client_id = c.client_id
GROUP BY c.client_id, Client_Name, transaction_month, transaction_year
HAVING monthly_transaction_count > 10 OR (MONTH(NOW()) = transaction_month AND monthly_transaction_count IS NOT NULL);
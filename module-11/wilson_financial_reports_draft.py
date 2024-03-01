"""
Jaci Brown, Amanda Riley, Gabriel Sanchez-Jorgensen, Hlee Xiong
2/29/24
CS310-O316
Module 11 Assignment
Group 9- Milestone 3
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "wilson_user",
    "password": "money",
    "host": "127.0.0.1",
    "database": "wilson_financial",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n   Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)


cursor = db.cursor(dictionary=True)  
cursor.execute("""
              SELECT CONCAT(f_name, ' ', l_name) AS Client_Name, MONTHNAME(date_added) AS Month_Added
              FROM clients 
              WHERE date_added >= '2023-09-01' AND date_added < '2024-03-01';
              """)
clients = cursor.fetchall()
print("\n-- DISPLAYING CLIENTS ADDED FOR PAST SIX MONTHS --\n")
for client in clients:
    print(f"{client['Client_Name']} - {client['Month_Added']}")


cursor.execute("""
              SELECT FORMAT(AVG(total_assets), 2) AS average_assets
              FROM (
                  SELECT c.client_id, SUM(t.amount) AS total_assets
                  FROM clients c
                  LEFT JOIN transactions t ON c.client_id = t.client_id
                  GROUP BY c.client_id
              ) AS client_assets;
              """)
result_2 = cursor.fetchall()
print("\n-- DISPLAYING AVERAGE AMOUNT OF ASSETS FOR ALL CLIENTS--\n")
for row in result_2:
    print(f"Average Assets: ${row['average_assets']}")


cursor.execute("""
              SELECT CONCAT(c.f_name, ' ', c.l_name) AS Client_Name,
                     COUNT(t.trans_id) AS monthly_transaction_count,
                     MONTH(t.transaction_date) AS transaction_month,
                     YEAR(t.transaction_date) AS transaction_year
              FROM clients c
              LEFT JOIN transactions t ON t.client_id = c.client_id
              GROUP BY c.client_id, Client_Name, transaction_month, transaction_year
              HAVING monthly_transaction_count > 10 OR (MONTH(NOW()) = transaction_month AND monthly_transaction_count IS NOT NULL);
              """)
result_3 = cursor.fetchall()
print("\n-- DISPLAYING ALL CLIENTS WITH HIGH NUMBER OF TRANSACTIONS--\n")
for row in result_3:
    print(f"{row['Client_Name']} - Transactions: {row['monthly_transaction_count']} - Month: {row['transaction_month']}, Year: {row['transaction_year']}")


db.close()





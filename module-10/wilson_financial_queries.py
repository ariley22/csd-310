"""
Jaci Brown, Amanda Riley, Gabriel Sanchez-Jorgensen, Hlee Xiong
2/23/24
CS310-O316
Module 10 Assignment
Group 9- Milestone 2
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
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()
cursor.execute("SELECT client_id, f_name, l_name, date_added FROM clients")
clients = cursor.fetchall()
print("-- DISPLAYING Client RECORDS --")
for client in clients:
    print("Client ID: {}\nClient Name: {} {}\nDate Added: {}\n\n".format(client[0], client[1], client[2], client[3]))

cursor.execute("SELECT account_id, account_type FROM accounts")
accounts = cursor.fetchall()
print("-- DISPLAYING Account RECORDS --")
for account in accounts:
    print("Account ID: {}\nAccount Type: {}\n\n".format(account[0], account[1]))

cursor.execute("SELECT trans_id, transaction_date, amount FROM transactions")
transactions = cursor.fetchall()
print("-- DISPLAYING Transaction RECORDS --")
for transaction in transactions:
    print("Transaction ID: {}\nDate: {}\nAmount: {}\n\n".format(transaction[0], transaction[1], transaction[2]))

db.close()
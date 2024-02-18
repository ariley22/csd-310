import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
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
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n\n".format(studio[0], studio[1]))

cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n\n".format(genre[0], genre[1]))

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime<120")
films = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS --")
for film in films:
    print("Film Name: {}\nRuntime: {}\n\n".format(film[0], film[1]))

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
directors = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --")
for director in directors:
    print("Film Name: {}\nDirector: {}\n\n".format(director[0], director[1]))

db.close()
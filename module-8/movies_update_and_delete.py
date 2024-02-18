def show_films(cursor, title):
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def main():
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

    show_films(cursor, "DISPLAYING FILMS")

    cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES('The Day After Tomorrow', 'Roland Emmerich', 2, 1, 2004, 123)")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    db.close()

if __name__ == "__main__":
    main()
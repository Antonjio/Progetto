import sqlite3
from flask import Blueprint, g, render_template

from server.auth import connect_db

# Create a Flask Blueprint for the "videogames" module
videogames = Blueprint('videogames', __name__)


# Define a route for the home page displaying all videogames
@videogames.route('/videogames')
def videogames_home():
    # Connect to the SQLite database
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve all games, ordered by release date in descending order
    query = """
            SELECT * FROM game
            ORDER BY game_release DESC
        """
    cursor.execute(query)

    # Fetch all records from the database
    giochi = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Render the HTML template with the retrieved data
    return render_template("videogames/videogames.html", giochi=giochi)


# Define a route for sorting videogames by price in ascending order
@videogames.route('/videogames/price/asc')
def videogamesASC():
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve all games, ordered by price in ascending order
    query = """
            SELECT * FROM game
            ORDER BY game_price ASC
        """
    cursor.execute(query)

    giochi = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("videogames/videogamesAsc.html", giochi=giochi)


# Define a route for sorting videogames by price in descending order
@videogames.route('/videogames/price/desc')
def videogamesDESC():
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve all games, ordered by price in descending order
    query = """
            SELECT * FROM game
            ORDER BY game_price DESC
        """
    cursor.execute(query)

    giochi = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("videogames/videogamesDESC.html", giochi=giochi)


# Define a route for displaying videogames of the "action" genre
@videogames.route('/videogames/genre/action')
def videogamesGenreAction():
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve games of the "action" genre
    query = """
            SELECT * FROM game
            WHERE genre = 'azione'
        """
    cursor.execute(query)

    giochi = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("videogames/videogamesAction.html", giochi=giochi)


# Define a route for displaying videogames of the "adventure" genre
@videogames.route('/videogames/genre/adventure')
def videogamesGenreAdventure():
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve games of the "adventure" genre
    query = """
            SELECT * FROM game
            WHERE genre = 'avventura'
        """
    cursor.execute(query)

    giochi = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("videogames/videogamesAdventure.html", giochi=giochi)


# Define a route for displaying videogames of the "sport" genre
@videogames.route('/videogames/genre/sport')
def videogamesGenreSport():
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve games of the "sport" genre
    query = """
            SELECT * FROM game
            WHERE genre = 'sport'
        """
    cursor.execute(query)

    giochi = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("videogames/videogamesSport.html", giochi=giochi)

@videogames.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()

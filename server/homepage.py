import sqlite3
from turtle import home
from flask import Blueprint, g, render_template

from server.auth import connect_db

# Create a Flask Blueprint for the "homepage" module
homepage = Blueprint('homepage', __name__)


# Define a route for the homepage
@homepage.route('/')
def index():
    # Connect to the SQLite database
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve the latest 9 games ordered by release date
    query = """
        SELECT * FROM game
        ORDER BY game_release DESC
        LIMIT 9;
    """
    cursor.execute(query)

    # Fetch the data from the first query
    giochi = cursor.fetchall()

    # Query to retrieve the cheapest 9 games (price < 40.00) ordered by price
    query2 = """
       SELECT * FROM game where game_price < 40.00
       ORDER BY game_price ASC
       LIMIT 9;
    """
    cursor.execute(query2)

    # Fetch the data from the second query
    giochi2 = cursor.fetchall()

    # Query to retrieve the 9 games with PEGI rating less than or equal to 12, ordered by PEGI rating
    query3 = """
          SELECT * FROM game where pegi <= 12
          ORDER BY pegi ASC
          LIMIT 9;
      """
    cursor.execute(query3)

    # Fetch the data from the third query
    giochi3 = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Pass the retrieved data to the template
    return render_template("index.html", giochi=giochi, giochi2=giochi2, giochi3=giochi3)

@homepage.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()

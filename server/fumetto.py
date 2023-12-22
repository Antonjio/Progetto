import sqlite3
from flask import Blueprint, g, render_template

from server.auth import connect_db

# Create a Blueprint named 'fumetto'
fumetto = Blueprint('fumetto', __name__)

# Route for displaying the main fumetto page
@fumetto.route('/fumetto')
def fumetto_home():
    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve fumetto data from the database, ordered by release date in descending order
    query = """
               SELECT * FROM fumetto
               ORDER BY comics_release DESC
           """
    cursor.execute(query)

    # Retrieve data from the database
    fumetto = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the fumetto home template with the retrieved data
    return render_template("fumetto/fumetto.html", fumetto=fumetto)

# Route for displaying fumetto data in ascending order of price
@fumetto.route('/fumetto/price/asc')
def fumettoAsc():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve fumetto data from the database, ordered by price in ascending order
    query = """
               SELECT * FROM fumetto
               ORDER BY comics_price ASC
           """
    cursor.execute(query)

    # Retrieve data from the database
    fumetto = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the fumettoAsc template with the retrieved data
    return render_template("fumetto/fumettoAsc.html", fumetto=fumetto)

# Route for displaying fumetto data in descending order of price
@fumetto.route('/fumetto/price/desc')
def fumettoDesc():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve fumetto data from the database, ordered by price in descending order
    query = """
               SELECT * FROM fumetto
               ORDER BY comics_price DESC
           """
    cursor.execute(query)

    # Retrieve data from the database
    fumetto = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the fumettoDesc template with the retrieved data
    return render_template("fumetto/fumettoDesc.html", fumetto=fumetto)

# Route for displaying fumetto data of type 'manga'
@fumetto.route('/fumetto/type/manga')
def fumettoManga():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve fumetto data from the database of type 'manga'
    query = """
               SELECT * FROM fumetto where comics_type = 'manga'
           """
    cursor.execute(query)

    # Retrieve data from the database
    fumetto = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the fumettoManga template with the retrieved data
    return render_template("fumetto/fumettoManga.html", fumetto=fumetto)

# Route for displaying fumetto data of type 'comics'
@fumetto.route('/fumetto/type/comics')
def fumettoComics():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve fumetto data from the database of type 'comics'
    query = """
               SELECT * FROM fumetto where comics_type = 'comics'
           """
    cursor.execute(query)

    # Retrieve data from the database
    fumetto = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the fumettoComics template with the retrieved data
    return render_template("fumetto/fumettoComics.html", fumetto=fumetto)

@fumetto.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()
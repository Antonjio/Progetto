import sqlite3
from flask import Blueprint, render_template

from server.auth import connect_db

# Create a Blueprint named 'funko'
funko = Blueprint('funko', __name__)

# Route for displaying the main funko page, ordered by release date in descending order
@funko.route('/funko')
def funko_home():
    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database, ordered by release date in descending order
    query = """
              SELECT * FROM funko_pop
              ORDER BY fun_release DESC
          """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funko home template with the retrieved data
    return render_template("funko/funko.html", funko=funko)

# Route for displaying funko data in ascending order of price
@funko.route('/funko/price/asc')
def funkoASC():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database, ordered by price in ascending order
    query = """
            SELECT * FROM funko_pop
            ORDER BY fun_price ASC
        """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funkoAsc template with the retrieved data
    return render_template("funko/funkoAsc.html", funko=funko)

# Route for displaying funko data in descending order of price
@funko.route('/funko/price/desc')
def funkoDesc():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database, ordered by price in descending order
    query = """
            SELECT * FROM funko_pop
            ORDER BY fun_price DESC
        """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funkoDesc template with the retrieved data
    return render_template("funko/funkoDesc.html", funko=funko)

# Route for displaying funko data of category 'serietv'
@funko.route('/funko/category/serietv')
def funkoCategorySerietv():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database of category 'serietv'
    query = """
            SELECT * FROM funko_pop
            WHERE category = 'serietv'
        """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funkoSerieTv template with the retrieved data
    return render_template("funko/funkoSerieTv.html", funko=funko)

# Route for displaying funko data of category 'film'
@funko.route('/funko/category/film')
def funkoCategoryFilm():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database of category 'film'
    query = """
            SELECT * FROM funko_pop
            WHERE category = 'film'
        """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funkoFilm template with the retrieved data
    return render_template("funko/funkoFilm.html", funko=funko)

# Route for displaying funko data of category 'game'
@funko.route('/funko/category/game')
def funkoCategoryGame():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve funko data from the database of category 'game'
    query = """
            SELECT * FROM funko_pop
            WHERE category = 'game'
        """
    cursor.execute(query)

    # Retrieve data from the database
    funko = cursor.fetchall()
    cursor.close()
    conn.close()

    # Render the funkoGame template with the retrieved data
    return render_template("funko/funkoGame.html", funko=funko)

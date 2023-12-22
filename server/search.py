from flask import Flask, g, render_template, request, jsonify, Blueprint, redirect
import sqlite3

from server.auth import connect_db

# Create a Blueprint named 'search'
search = Blueprint('search', __name__)

# Route for handling the search functionality
@search.route('/search')
def search_products():
    # Get the search term from the query parameters
    term = request.args.get('term')

    # Perform the search in the game, funko_pop, and fumetto tables
    results = search_in_database(term)

    # If there are no results, render a template with the results message
    if not any(results.values()):
        return render_template('results.html', results=results)

    # Otherwise, redirect to a new page with the search results
    return redirect('/results?term=' + term)

# Function to search the database for the specified term
def search_in_database(term):
    # Connect to the database (ensure your connection is configured correctly)
    conn = connect_db()
    cursor = conn.cursor()

    # Execute search queries in the game, funko_pop, and fumetto tables
    cursor.execute("SELECT * FROM game WHERE game_name LIKE ?", ('%' + term + '%',))
    giochi = cursor.fetchall()

    cursor.execute("SELECT * FROM funko_pop WHERE fun_name LIKE ?", ('%' + term + '%',))
    funko_pop = cursor.fetchall()

    cursor.execute("SELECT * FROM fumetto WHERE comics_name LIKE ?", ('%' + term + '%',))
    fumetti = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the search results
    return {'giochi': giochi, 'funko_pop': funko_pop, 'fumetti': fumetti}

# Route for displaying the search results
@search.route('/results')
def display_results():
    # Get the search term from the query parameters
    term = request.args.get('term')

    # Get the results from the search function
    results = search_in_database(term)

    # Pass the results to the HTML template
    return render_template('results.html', results=results)


@search.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()
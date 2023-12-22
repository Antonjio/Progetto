import os
from flask import Blueprint, g, render_template, request, redirect, session, make_response, jsonify
import sqlite3

from server.auth import connect_db

# Table cart indexes
CART_ID = 0
ITEM_ID = 1
TIME = 2
USER = 3

# Table game indexes
ean_game = 0
game_name = 1
game_price = 2
game_release = 3
genre = 4
pegi = 5
sh_name = 6
image = 7

# Table fumetto indexes
ean_comics = 0
comics_name = 1
comics_price = 2
comics_release = 3
comics_type = 4
pages = 5
author = 6
image = 7
editor_name = 8

# Table funko_pop indexes
FUNKO_EAN = 0
fun_name = 1
fun_price = 2
fun_release = 3
height = 4
depthA = 5
width = 6
image = 7
category = 8

# Create a Blueprint named 'cart'
cart = Blueprint('cart', __name__)

# Connect to the SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")
connection = sqlite3.connect(DB_PATH, check_same_thread=False)
db = connection.cursor()

# Route for displaying the cart page
@cart.route('/cart')
def cart_page():
    if 'user' in session:
        # Render the cart page template
        return render_template('cart/cart.html')
    else:
        return jsonify({'error': 'User not logged in'})

# Route for retrieving items in the cart
@cart.route('/cart/items')
def cart_items():
    user_id = session['user'][7]

    # Fetch items from different tables (game, fumetto, funko_pop) based on user_id
    # Convert items into a standardized format for response

    gameCart = db.execute("SELECT * FROM cart INNER JOIN game ON cart.item_id = game.ean_game WHERE cart.user = ?", (user_id,)).fetchall()
    cartFumetto = db.execute("SELECT * FROM cart INNER JOIN fumetto ON cart.item_id = fumetto.ean_comics WHERE cart.user = ?", (user_id,)).fetchall()
    cartFunko = db.execute("SELECT * FROM cart INNER JOIN funko_pop ON cart.item_id = funko_pop.funko_ean WHERE cart.user = ?", (user_id,)).fetchall()

    all_items = []
    # Append items from the gameCart to the all_items list
    for item in gameCart:
        item_dict = {
            'data_aggiunta': item[TIME],
            'ean': item[ean_game + 4],
            'name': item[game_name + 4],
            'prezzo': item[game_price + 4],
            'data_uscita': item[game_release + 4],
            'game_genre': item[genre + 4],
            'game_pegi': item[pegi + 4],
            'game_sh': item[sh_name + 4],
            'image': item[image + 4]
        }
        all_items.append(item_dict)
    # Append items from the cartFumetto to the all_items list
    for item in cartFumetto:
        item_dict = {
            'data_aggiunta': item[TIME],
            'ean': item[ean_comics + 4],
            'name': item[comics_name + 4],
            'prezzo': item[comics_price + 4],
            'data_uscita': item[comics_release + 4],
            'comics_type': item[comics_type + 4],
            'pages_fumetto': item[pages + 4],
            'author_fumetto': item[author + 4],
            'image': item[image + 4],
            'editor_name_fumetto': item[editor_name + 4]
        }
        all_items.append(item_dict)
    # Append items from the cartFunko to the all_items list
    for item in cartFunko:
        item_dict = {
            'data_aggiunta': item[TIME],
            'ean': item[FUNKO_EAN + 4],
            'name': item[fun_name + 4],
            'prezzo': item[fun_price + 4],
            'data_uscita': item[fun_release + 4],
            'height_funko': item[height + 4],
            'deptha_funko': item[depthA + 4],
            'width_funko': item[width + 4],
            'image': item[image +4],
            'category_funko': item[category + 4]
        }
        all_items.append(item_dict)

    result_json = jsonify(all_items)

    return result_json


# Route for adding items to the cart
@cart.route('/store', methods=['POST'])
def store_cart():
    try:
        if 'user' in session:
            # Retrieve user_id and item_id from the form data
            user_id = session['user'][7]
            item_id = request.form.get("item_id", None)

            # Check if the item is already in the user's cart
            item = db.execute("SELECT item_id FROM cart WHERE item_id = ? AND user = ?", (item_id, user_id)).fetchone()

            if item:
                # Return response indicating that the item is already added
                return make_response(jsonify({'already_added': 'The item has already been added to the cart'}))
            else:
                # Insert the item into the cart and commit changes
                db.execute("INSERT INTO cart (item_id, user) VALUES (?, ?)", (item_id, user_id))
                connection.commit()

                # Return success response with redirect URL
                return jsonify({'success': True, 'redirect_url': '/cart'})
        else:
            # Return response indicating that the user is not logged in
            return jsonify({'not_logged': 'User not logged in'})

    except Exception as e:
        print(e)
        # Return response indicating an error
        return jsonify({'error': 'Error'})


# Route for removing items from the cart
@cart.route('/remove/<product_ean>', methods=['POST'])
def remove_from_cart(product_ean):
    try:
        user_id = session['user'][7]

        # Remove the item from the cart in the database
        db.execute("DELETE FROM cart WHERE item_id = ? AND user = ?", (product_ean, user_id))
        connection.commit()

        # Redirect to the cart page
        return redirect('/cart')

    except Exception as e:
        print(f"Error removing from cart: {e}")

        # Return response indicating an error during removal
        return 'Error removing from cart'


# Function to empty the entire cart
def empty_cart():
    try:
        user_id = session['user'][7]

        # Empty the cart in the database
        db.execute("DELETE FROM cart WHERE user = ?", (user_id,))
        connection.commit()

        # Return success response
        return jsonify({'success': True})

    except Exception as e:
        print(f"Error emptying the cart: {e}")

        # Return response indicating an error during cart emptying
        return jsonify({'error': 'Error'})
@cart.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()
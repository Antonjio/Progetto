import os
import sqlite3
from flask import Blueprint, g, jsonify, make_response, request, session
from werkzeug.security import generate_password_hash, check_password_hash

# users tuples indexes
name = 0
lastname = 1
number = 2
country = 3
address = 4
PASSWORD = 5
birthdate = 6
EMAIL = 7
USERNAME = 8

# Create a Blueprint named 'auth'
auth = Blueprint('auth', __name__)

def connect_db():
    """ function to connect to database """
    if 'db' not in g:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(BASE_DIR, "db", "database.db")
        g.db = sqlite3.connect(DB_PATH)
    return g.db

# Route for user login
@auth.route('/login', methods=['POST'])
def login():
    # Retrieve email and password from the form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Connect to the SQLite database
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the user exists in the database
    cursor.execute('SELECT * FROM users WHERE email=?', (email,))
    existing_user = cursor.fetchone()

    conn.commit()
    conn.close()

    # Validate the user credentials
    if existing_user:
        if check_password_hash(existing_user[PASSWORD], password):
            # Set user session and return success message
            session['user'] = existing_user
            return jsonify({'success': 'Welcome back'})
        else:
            return jsonify({'warning': 'Incorrect password'})
    else:
        return jsonify({'error': 'User not registered'})

# Route for user registration
@auth.route('/registration', methods=['POST'])
def registration():
    # Retrieve user registration data from the form
    name = request.form.get("firstName")
    lastname = request.form.get("lastName")
    data_di_nascita = request.form.get("birthdate")
    number = request.form.get("phoneNumber")
    country = request.form.get("country")
    address = request.form.get("address")
    username = request.form.get("username")
    password = request.form.get("signupPassword")
    email = request.form.get("signupEmail")

    # Connect to the SQLite database
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the username or email is already in use
    cursor.execute('SELECT * FROM users WHERE username=? or email=?', (username, email,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        error_message = "Email/username already in use"
        return jsonify({'error': error_message})
    else:
        # Hash the password and add the new user to the database
        hashed_password = generate_password_hash(password=password, method='pbkdf2:sha256')
        cursor.execute(
            'INSERT INTO users (name,lastname,number,country,address,password,birthdate,email,username) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (name, lastname, number, country, address, hashed_password, data_di_nascita, email, username,))

        # Retrieve the newly registered user and set the session
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cursor.fetchone()
        session['user'] = user

        conn.commit()
        conn.close()

        return jsonify({'success': 'User registered'})

# Route to retrieve user information
@auth.route('/user', methods=['GET'])
def user():
    # Check if the user is logged in
    if 'user' not in session:
        return make_response(jsonify({'message': 'User not logged in', 'status': 401}))

    # Retrieve user data from the session
    user = session['user']

    # Prepare user data for response
    user_data = {
        'firstName': user[name],
        'lastName': user[lastname],
        'phoneNumber': user[number],
        'country': user[country],
        'address': user[address],
        'birthDate': user[birthdate],
        'email': user[EMAIL],
        'username': user[USERNAME]
    }

    # Return user data in the response
    return make_response(jsonify({'user': user_data, 'status': 200}))

# Route for user logout
@auth.route('/logout', methods=['POST'])
def logout():
    # Check if the user is logged in
    if 'user' in session:
        # Remove user session and return success message
        session.pop('user', None)
        return make_response(jsonify({'message': 'User logged out successfully', 'status': 200}))
    else:
        # Return a message indicating that the user is not logged in
        return make_response(jsonify({'message': 'User not logged in', 'status': 401}))

@auth.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()

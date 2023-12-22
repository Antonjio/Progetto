import secrets

from flask import Flask
from server.auth import auth
from server.homepage import homepage
from server.videogames import videogames
from server.funko import funko
from server.fumetto import fumetto
from server.search import search
from server.cart import cart
from server.checkout import checkout
from server.sw import sw
from server.components import components


def generate_secret_key(length=32):
    """
    Generate a secure random key for use in Flask sessions.

    Parameters:

    - length: The length of the key (default is 32).

      Returns:
      A securely generated key."""

    return secrets.token_hex(length // 2)


def regenerate_secret_key(app):
    app.secret_key = generate_secret_key()
    print('secret key regenereted')


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.register_blueprint(auth)
    app.register_blueprint(homepage)
    app.register_blueprint(videogames)
    app.register_blueprint(fumetto)
    app.register_blueprint(funko)
    app.register_blueprint(search)
    app.register_blueprint(cart)
    app.register_blueprint(checkout)
    app.register_blueprint(sw)
    app.register_blueprint(components)

    app.secret_key = generate_secret_key()
    return app

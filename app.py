import time

from server import create_app, regenerate_secret_key
from flask import redirect, render_template, session, request
import sqlite3

SECRET_KEY_REGENERATION_INTERVAL = 3600

app = create_app()


@app.before_request
def before_request():
    last_regeneration_time = time.time()

    elapsed_time = time.time() - last_regeneration_time
    if elapsed_time > SECRET_KEY_REGENERATION_INTERVAL:
        regenerate_secret_key(app=app)
        last_regeneration_time = time.time()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

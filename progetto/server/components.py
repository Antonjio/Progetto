from flask import Blueprint, render_template

components = Blueprint('components', __name__)


@components.route('/navbar')
def navbar():
  """ route to get navbar component """
  return render_template('navbar.html')

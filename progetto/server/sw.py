from flask import Blueprint, send_from_directory

sw = Blueprint('sw', __name__)


@sw.route('/sw')
def get_service_worker():
  return send_from_directory('../static', 'sw.js')

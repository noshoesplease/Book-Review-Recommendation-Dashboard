from flask import Blueprint

bp = Blueprint('rec_sys', __name__, template_folder='templates')

from app.rec_sys import routes
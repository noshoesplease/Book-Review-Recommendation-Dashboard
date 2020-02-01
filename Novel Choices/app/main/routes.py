from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from app import db
from app.main import bp


# before request check if we're
# working with local storage
# if yes, check associated directories for seeded data
#   if exists, pass
#   else populate
# else setup cloud pipeline
@bp.route('/')
def main():
    return render_template('main.html', title='Big Data Algorithms Project')
              

from flask import render_template, flash, redirect, \
url_for, request, json
from werkzeug.urls import url_parse
from app import db
from app.dashboard import bp

@bp.route('/dashboard')
def dashboard():
    stats = []
    return render_template('dashboard.html', title='Big Data Algorithms Project', stats=stats)





"""
the dashbaoard will be composed from several handler functions
that each take care of rendering the graph on full 
html pages like in Dash. So the UI is made from a bunch of
rendered graphs, each having their own web pages.
On the UI we can postion and size them in the section tag
using iFrames.
"""


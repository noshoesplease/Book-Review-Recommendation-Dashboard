from flask import render_template, flash, redirect, \
url_for, request
from werkzeug.urls import url_parse
from app import db
from app.report import bp

@bp.route('/report')
def report():
    return render_template('report.html', title='Big Data Algorithms Project')
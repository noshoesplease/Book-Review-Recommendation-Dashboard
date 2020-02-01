from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, session
from app import db
from app.database.models import Book, User, Rating
from app.rec_sys import bp


def get_prediction(books, ratings):
    return Book.query.all()[:10]

@bp.route('/rec_sys', methods=['GET', 'POST'])
def rec_sys():

    books = Book.query.all()[:10]

    if request.method == 'POST':
        keys = [key for key in request.form.keys()]
        ratings = []
        for i in range(5):
            ratings.append(request.form[keys[i]])
            db.session.add(
                Rating(
                    overall=ratings[i],
                    book_id=books[i].id,
                    user_id=0
                )
            )
        db.session.commit()
        session['books'] = {
            'book0': books[0].asin,
            'book1': books[1].asin,
            'book2': books[2].asin,
            'book3': books[3].asin,
            'book4': books[4].asin

        }
        session['ratings'] = {
            'rating0': ratings[0],
            'rating1': ratings[1],
            'rating2': ratings[2],
            'rating3': ratings[3],
            'rating4': ratings[4]
        }

    return render_template('rec_sys.html',title='Big Data Algorithms Project',books=books)

@bp.route('/prediction')
def prediction():
    print(session['ratings'])

    results = get_prediction(None,None)
    return render_template('results.html',title='Big Data Algorithms Project', results=results)
    
@bp.route('/book/<asin>')
def book(asin):
    return render_template(
        'book.html',
        title='Big Data Algorithms Project',
        book=Book.query.filter_by(asin=asin).all()[0]
    )
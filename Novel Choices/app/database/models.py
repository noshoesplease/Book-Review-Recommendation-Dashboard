from datetime import datetime
from app import db
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_of_creation = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reviewer_id = db.Column(db.String(64), index=True, unique=True, default=None)
    reviewer_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True, default=None)
    password = db.Column(db.String(64), index=True, default=None)
    
    def __repr__(self):
        return '<User\nName={}\nDate of Creation={}\Reviewer ID={}'.format(self.reviewer_name, self.date_of_creation, self.reviewer_id)

def load_user(id):
    return User.query.get(int(id))

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    date_of_creation = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    asin = db.Column(db.String(32), index=True)
    title = db.Column(db.String(128), index=True)
    price = db.Column(db.String(32), index=True, default=None)
    imUrl = db.Column(db.String(128), index=True, default=None)
    description = db.Column(db.String(1024), default=None)
    sales_rank = db.Column(db.String(32), index=True, default=None)
    also_bought = db.Column(db.String(32), default=None)
    also_viewed = db.Column(db.String(32), default=None)
    bought_together = db.Column(db.String(32), default=None)
    buy_after_viewing = db.Column(db.String(32), default=None)

    def __repr__(self):
        return '<Book\nBook ID={}\nTitle={}\ASIN={}>'.format(self.id, self.title, self.asin)

def load_book(id):
    return Book.query.get(int(id))

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    date_of_creation = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    overall = db.Column(db.Integer, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), index=True)
    
    # use this for now until user registration is implemented
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, default=None)

    # TODO:implement user registration so we dont
    # have to keep null record of the user in the ratings table
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)

    # Define relationship to user
    user = db.relationship('User', backref=db.backref('ratings', order_by=id))

    # Define relationship to book
    book = db.relationship('Book', backref=db.backref('ratings', order_by=id))

    def __repr__(self):
        return '<Rating\nRating ID={}\nRating={}\nBook ID={}\nuUser ID={}'.format(self.id, self.overall, self.book_id, self.user_id)

def load_rating(id):
    return Rating.query.get(int(id))
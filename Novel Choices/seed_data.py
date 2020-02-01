from BDAProject import app
from app.database.models import Book, User, Rating
from BDAProject import db
import json
from app import create_app

app = create_app()
app.app_context().push()

def retrieve_books_from_JSON():
    path = 'app/data_services/data/book_meta_data_chunk28.json'
    with open(path, 'r') as j:
        book_list = j.readlines()
    for book in book_list:
        if book == '\n':
            book_list.remove(book)
    return book_list

def retrieve_users_from_JSON():
    path = 'app/data_services/data/unique_reviewer_chunk22.json'
    with open(path, 'r') as j:
        user_list = j.readlines()
    for user in user_list:
        if user == '\n':
            user_list.remove(user)
    return user_list

def retrieve_ratings_from_JSON():
    path = 'app/data_services/data/book_data_chunk22.json'
    with open(path, 'r') as j:
        rating_list = j.readlines()
    for rating in rating_list:
        if rating == '\n':
            rating_list.remove(rating)
    return rating_list

def load_books():
    print('Loading books...')

    Book.query.delete()
    books = retrieve_books_from_JSON()
    
    no_data = 'No data is available.'
    for book in books:
        book = json.loads(book)
        asin = book['asin']
        title = book['title']
        if 'price' in book.keys():
            price = book['price']
        else:
            price = no_data
        if 'imUrl' in book.keys():
            imUrl = book['imUrl']
        else:
            imUrl = no_data
        if 'description' in book.keys():
            description = book['description']
        else:
            description = no_data
        if 'salesRank' in book.keys():
            sales_rank = book['salesRank']['Books']
        else:
            sales_rank = no_data
        if 'related' in book.keys():
            if 'also_bought' in book['related'].keys():
                also_bought = book['related']['also_bought'][0]
            else:
                also_bought = no_data
            if 'also_viewed' in book['related'].keys():
                also_viewed = book['related']['also_viewed'][0]
            else:
                also_viewed = no_data
            if 'bought_together' in book['related'].keys():
                bought_together = book['related']['bought_together'][0]
            else:
                bought_together = no_data
            if 'buy_after_viewing' in book['related'].keys():
                buy_after_viewing = book['related']['buy_after_viewing'][0]
            else:
                buy_after_viewing = no_data
        
        book = Book(
            asin=asin,
            title=title,
            price=price,
            imUrl=imUrl,
            description=description,
            sales_rank=sales_rank,
            also_bought=also_bought,
            also_viewed=also_viewed,
            bought_together=bought_together,
            buy_after_viewing=buy_after_viewing
        )
        db.session.add(book)
    
    db.session.commit()

def load_users():
    print('Loading users...')

    User.query.delete()
    users = retrieve_users_from_JSON()
    
    for user in users:
        user = json.loads(user)
        reviewer_id = user['reviewerID']
        reviewer_name = user['reviewerName']
        
        user = User(
            reviewer_id=reviewer_id,
            reviewer_name=reviewer_name
        )
        db.session.add(user)
    
    db.session.commit()

def load_ratings():
    print('Loading ratings...')

    Rating.query.delete()
    ratings = retrieve_ratings_from_JSON()
    
    for rating in ratings:
        rating = json.loads(rating)
        overall = rating['overall']
        asin = rating['asin']
        reviewer_id = rating['reviewerID']

        user = User.query.filter_by(reviewer_id=reviewer_id).first()
        book = Book.query.filter_by(asin=asin).first() 
        if book:
            rating = Rating(
                overall=overall,
                user_id=user.id,
                book_id=book.id
            )

            db.session.add(rating)

    db.session.commit()



load_books()
load_users()
# do not call until we can 
# query Book with an ASIN found in Ratings.
# right now there is not enough overlap between the data
load_ratings()

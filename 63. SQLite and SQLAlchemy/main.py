from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.app_context().push()
db = sqlite3.connect("Martyna's books collection.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# # # cursor.execute("INSERT INTO books VALUES(2, 'JASIEK NA WAKACJACH', 'J. Sobus', '10')")
# # cursor.execute("INSERT INTO books VALUES(4, 'moda', 'sukces', '1')")
# db.commit()
# print(os.path.abspath("new-books-collection.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///Martyna's books collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title
# db.create_all() does not update tables if they are already in the database. 
# db.create_all() 

 

@app.route('/')
def start():
    try:
        all_books = db.session.execute(db.select(Book)).all()
    except:
        all_books = []  
    
    return render_template('index.html', all_books=all_books)

@app.route("/home")
def home():
    all_books = db.session.execute(db.select(Book)).all()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods = ['POST', 'GET'])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["book_name"], 
            author=request.form["book_author"], 
            rating=request.form["rating"],
            )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html' )

@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id= request.args.get('id')
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        print(book)
        new_rating=float(request.form["new_rating"][0]) 
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html',book=book) 

@app.route("/delete", methods=["POST","GET"])
def delete():
    book_id= request.args.get('id')
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))    

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()

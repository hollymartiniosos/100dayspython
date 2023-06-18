from flask import Flask, render_template, request, redirect, session, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3
from flask_sqlalchemy import SQLAlchemy

MOVIE_DB_API_KEY = "3df979b2"
MOVIE_DB_SEARCH_URL = "http://www.omdbapi.com/?i=tt1630029&apikey=3df979b2"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.app_context().push()
db = sqlite3.connect("Martyna's movies collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE Movie (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, year INT NOT NULL, description varchar(500) NOT NULL, rating FLOAT NOT NULL, ranking INT NOT NULL, review varchar(500) NOT NULL, img_url URL NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///Martyna's movies collection.db"
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable = False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(500), unique=False, nullable=False)
    img_url = db.Column(db.String(500), unique=True, nullable=False)


    def __repr__(self):
        return '<Movie %r>' % self.title

def add_manual():
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
    db.session.add(new_movie)
    db.session.commit()

# db.create_all() 
#add()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


@app.route('/')
def start():
    try:
        all_movies = db.session.execute(db.select(Movie)).all()
    except:
        all_movies = []  
    
    return render_template('index.html', all_movies=all_movies)

@app.route("/home")
def home():
    try:
        all_movies = db.session.execute(db.select(Movie)).all()
    except:
        all_movies = []  
    
    return render_template('index.html', all_movies=all_movies)



@app.route('/edit', methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html', movie=movie, form=form) 

@app.route("/delete", methods=["POST","GET"])
def delete():
    movie_id= request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))  



@app.route("/add", methods=["POST","GET"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()
        print(data)
        return render_template("select.html", options=data)
    return render_template('add.html',  form=form) 

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)

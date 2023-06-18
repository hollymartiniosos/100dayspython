from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.app_context().push()
db = sqlite3.connect("Martyna's db.db")
cursor = db.cursor()
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///Martyna's db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique= True)
    date_joined = db.Column(db.Date, default=datetime.now)

    def __repr__(self):
        return f'<User: {self.email}>'
    
   
db.create_all()    
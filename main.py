import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

class Base(DeclarativeBase):
    pass    

db = SQLAlchemy(model_class=Base)


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column(unique=False)
    rating: Mapped[float] = mapped_column(unique=False)

with app.app_context():
    db.create_all()

    book1 = Books(title="Harry Potter", author="J.K. Rowling", rating=9.3)
    db.session.add(book1)
    db.session.commit()
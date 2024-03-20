import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

db = SQLAlchemy()
Base = declarative_base()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(800)unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    synopsis = Column(String(200000))
    year = Column(Integer)
    time_line = Column(Integer)
    rating = Column(Float)
    image = Column(String(800))
    category = Column(String(80))
    review_id = Column(Integer, ForeignKey('review.id'))
    review = relationship(Review)

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    score = Column(Float)
    user_opinion = Column(String(10000))
    likes = Column(Integer)
    dislikes = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    movies_id = Column(Integer, ForeignKey('movie.id'))
    movies = relationship(Movie)
    
class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    movie = relationship(Movie)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

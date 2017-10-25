# coding=utf-8

# 1 - imports
from base import Session
from movie import Movie
from actor import Actor
from contact_details import ContactDetails
from stuntman import Stuntman

# 2 - extract a session
session = Session()

# 3 - extract movies
movies = session.query(Movie).all()

# 4 - log movies' details
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
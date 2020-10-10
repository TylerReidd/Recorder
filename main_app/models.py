from django.db import models

# Create your models here.
class Record: 
    def __init__(self, title, release_year, genre, review):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.review = review


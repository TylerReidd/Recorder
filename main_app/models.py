from django.db import models

# Create your models here.
class Record: 
    def __init__(self, title, release_year, genre, review):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.review = review

records = [
    Record('Aja', 1977, 'jazz-rock?', 'A reaally good album'),
    Record('blue', 1977, 'folk-jazz?', 'pretty good album. Good color'),
    Record('Sail Away', 1970, 'rock', 'one of the best ')
]
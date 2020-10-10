from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    review = models.CharField(max_length=1000)
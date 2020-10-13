from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Record(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    review = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})

class Song(models.Model):
    title = models.CharField(max_length=100)
    songwriter = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for record_id: {self.record_id} @{self.url}"
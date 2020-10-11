from django.db import models
from django.urls import reverse

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    review = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('detail', kwargs={'record_id': self.id})

class Song(models.Model):
    title = models.CharField(max_length=100)
    songwriter = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
=======
        return reverse('detail', kwargs={'record_id': self.id})
>>>>>>> 32f0a0296d1484c6f0d64eaf8a78e2c3c09839e9

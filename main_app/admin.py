from django.contrib import admin
from .models import Record, Song, Artist
# Register your models here.

admin.site.register(Record)
admin.site.register(Song)
admin.site.register(Artist)
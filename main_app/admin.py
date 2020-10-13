from django.contrib import admin
from .models import Record, Song, Photo
# Register your models here.

admin.site.register(Record)
admin.site.register(Song)
admin.site.register(Photo)
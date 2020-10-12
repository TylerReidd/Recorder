from django.forms import ModelForm
from .models import Song, Artist

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'songwriter']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'record', 'song']
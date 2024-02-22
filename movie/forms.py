from django import forms
from .models import Genre, Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name','description']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'duration', 'summary', 'genre']

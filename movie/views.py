# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie
from .forms import GenreForm, MovieForm

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'genre_detail.html', {'genre': genre, 'movies': movies})

def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'create_genre.html', {'form': form})

def update_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'update_genre.html', {'form': form, 'genre': genre})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'update_movie.html', {'form': form, 'movie': movie})

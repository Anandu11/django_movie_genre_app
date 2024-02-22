"""Picture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from movie.views import (
    genre_list, genre_detail, create_genre, update_genre,
    movie_list, movie_detail, create_movie, update_movie
)

urlpatterns = [
    path('genres/', genre_list, name='genre_list'),
    path('genres/<int:pk>/', genre_detail, name='genre_detail'),
    path('genres/create/', create_genre, name='create_genre'),
    path('genres/update/<int:pk>/', update_genre, name='update_genre'),

    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/create/', create_movie, name='create_movie'),
    path('movies/update/<int:pk>/', update_movie, name='update_movie'),
    
]




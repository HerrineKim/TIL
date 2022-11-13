import random
import requests
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def mainboard(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/mainboard.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):  
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')    

    movie = Movie()

    movie.title = title 
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    context = {
        'movie': movie
    }
    return redirect('movies:detail', movie.pk)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:mainboard')

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')    

    movie = Movie.objects.get(pk=pk)
    movie.title = title 
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    return redirect('movies:detail', movie.pk)

#####################################################

def index(request):
    url = 'https://api.themoviedb.org/3/movie/278/recommendations'
    params={
        'api_key' : 'b62f75c838cebf4e82c9634fae139c52',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(url, params=params).json()
    movies = response.get('results')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def recommendation(request):
    url = 'https://api.themoviedb.org/3/movie/278/recommendations'
    params={
        'api_key' : 'b62f75c838cebf4e82c9634fae139c52',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(url, params=params).json()
    movie = random.choice(response.get('results'))

    context = {
        'movie': movie,
    }

    return render(request, 'movies/recommendation.html', context)
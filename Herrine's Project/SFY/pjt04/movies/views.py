import random
import requests
from django.shortcuts import render
# Create your views here.

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
    return render(request, 'index.html', context)

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

    return render(request, 'recommendation.html', context)
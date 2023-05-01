from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .models import Movie
from .utils import search_movies


def home(request):
    movies, search_query = search_movies(request)
    last_added = Movie.objects.order_by('-pk')[:5]
    context = {
        'movies': movies,
        'last_added': last_added,
        'search_query': search_query
    }
    return render(request, 'home/index.html', context)


def get_movie(request, slug):
    movie_single = Movie.objects.get(url=slug)
    last_added = Movie.objects.order_by('-pk')[:5]
    context = {'movie_single': movie_single, 'last_added': last_added}
    return render(request, 'home/moviesingle.html', context)


def category_movies(request):
    movies = Movie.objects.filter(category=1)
    last_added = Movie.objects.filter(category=1).order_by('-pk')[:5]
    context = {'movies': movies, 'last_added': last_added}
    return render(request, 'home/index.html', context)


def category_series(request):
    series = Movie.objects.filter(category=2)
    last_added = Movie.objects.filter(category=2).order_by('-pk')[:5]
    context = {'movies': series, 'last_added': last_added}
    return render(request, 'home/index.html', context)


def category_cartoon(request):
    cartoon = Movie.objects.filter(category=3)
    last_added = Movie.objects.filter(category=3).order_by('-pk')[:5]
    context = {'movies': cartoon, 'last_added': last_added}
    return render(request, 'home/index.html', context)

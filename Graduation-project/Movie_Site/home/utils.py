from .models import Movie, Actor
from django.db.models import Q


def search_movies(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # actors = Actor.objects.filter(name__icontains=search_query)
    #
    # Q(directors__in=actors) |
    # Q(actors__in=actors))

    movies = Movie.objects.distinct().filter(Q(title__icontains=search_query) |
                                             Q(description__icontains=search_query) |
                                             Q(directors__name__icontains=search_query) |
                                             Q(actors__name__icontains=search_query))
    return movies, search_query

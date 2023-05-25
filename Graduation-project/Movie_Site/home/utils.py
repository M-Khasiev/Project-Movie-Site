from .models import Movie
from django.db.models import Q
from django.core.paginator import Paginator


def search_movies(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # actors = Actor.objects.filter(name__icontains=search_query)
    #
    # Q(directors__in=actors) |
    # Q(actors__in=actors))

    movies = Movie.objects.distinct().filter(Q(title__iregex=search_query) |
                                             Q(description__iregex=search_query) |
                                             Q(directors__name__iregex=search_query) |
                                             Q(actors__name__iregex=search_query))
    return movies, search_query


def paginate_movies(request, movies, results):
    page = request.GET.get('page', 1)
    # results = 6
    paginator = Paginator(movies, results, allow_empty_first_page=False)

    movies = paginator.get_page(page)

    left_index = int(page) - 2

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, movies


def selection_data_genres(request):
    movie_list = list()
    if request.GET.get('Thriller'):
        thriller = Movie.objects.filter(genres__name__icontains='Триллер')
        for i in thriller:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('Fantastic'):
        fantastic = Movie.objects.filter(genres__name__icontains='Фантастика')
        for i in fantastic:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('Comedy'):
        comedy = Movie.objects.filter(genres__name__icontains='Комедия')
        for i in comedy:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('Horror'):
        horror = Movie.objects.filter(genres__name__icontains='Ужасы')
        for i in horror:
            if i not in movie_list:
                movie_list.append(i)

    url_checkbox_genre = list()

    for i in request.GET:
        url_checkbox_genre.append(i)

    url_checkbox_genre = ''.join([f"{x}=on&" for x in url_checkbox_genre]).replace('page=on&', '')

    return movie_list, url_checkbox_genre


def selection_data_year(request):
    movie_list = list()
    if request.GET.get('2023'):
        year_2023 = Movie.objects.filter(year=2023)
        for i in year_2023:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('2022'):
        year_2022 = Movie.objects.filter(year=2022)
        for i in year_2022:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('2021'):
        year_2021 = Movie.objects.filter(year=2021)
        for i in year_2021:
            if i not in movie_list:
                movie_list.append(i)

    if request.GET.get('2016/2020'):
        years = Movie.objects.all()
        for i in years:
            if 2016 <= i.year <= 2020:
                if i not in movie_list:
                    movie_list.append(i)

    if request.GET.get('2011/2015'):
        years = Movie.objects.all()
        for i in years:
            if 2011 <= i.year <= 2015:
                if i not in movie_list:
                    movie_list.append(i)

    if request.GET.get('2001/2010'):
        years = Movie.objects.all()
        for i in years:
            if 2001 <= i.year <= 2010:
                if i not in movie_list:
                    movie_list.append(i)

    if request.GET.get('1985/2000'):
        years = Movie.objects.all()
        for i in years:
            if 1985 <= i.year <= 2000:
                if i not in movie_list:
                    movie_list.append(i)

    url_checkbox_year = list()

    for i in request.GET:
        url_checkbox_year.append(i)

    url_checkbox_year = ''.join([f"{x}=on&" for x in url_checkbox_year]).replace('page=on&', '').replace('/', '%2F')

    return movie_list, url_checkbox_year




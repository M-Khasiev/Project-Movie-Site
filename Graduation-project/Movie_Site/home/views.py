from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Actor
from .utils import paginate_movies, selection_data_genres, selection_data_year, true_body, last_added
from .forms import ReviewForm
from django.core.paginator import EmptyPage
from django.db.models import Q


def home(request):
    """Главная страница со всеми фильмами"""
    movies = Movie.objects.all()
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {
        'movies': movies,
        'last_added': last_added(),
        'custom_range': custom_range
    }
    return render(request, 'home/index.html', context)


def search_movie(request):
    """Поиск фильмов (по названию, английскому названию, по режиссёрам и актёрам)"""
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    url_search_query = f"search_query={search_query}&"
    movies = Movie.objects.distinct().filter(Q(title__iregex=search_query) |
                                             Q(eng_title__iregex=search_query) |
                                             Q(directors__name__iregex=search_query) |
                                             Q(actors__name__iregex=search_query))
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range,
               'search': url_search_query
               }
    return render(request, 'home/index.html', context)


def get_movie(request, slug):
    """Полная информация о фильме"""
    movie_single = Movie.objects.get(url=slug)
    review_body_check = true_body(slug)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie_single
            review.owner = request.user
            review.save()

            movie_single.get_vote_count()

            messages.success(request, 'Ваш отзыв успешно отправлен!')
            return redirect(movie_single.get_absolute_url())
        else:
            messages.error(request, form.errors)
            return redirect(movie_single.get_absolute_url())

    context = {
        'movie_single': movie_single,
        'last_added': last_added(),
        'form': form,
        'review_body_check': review_body_check
    }
    return render(request, 'home/moviesingle.html', context)


def category_movies(request):
    """Вывод всех фильмов"""
    movies = Movie.objects.filter(category=1)
    last_added_movies = Movie.objects.filter(category=1).order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added_movies})
    context = {'movies': movies,
               'last_added': last_added_movies,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def category_series(request):
    """Вывод всех сериалов"""
    series = Movie.objects.filter(category=2)
    last_added_series = Movie.objects.filter(category=2).order_by('-pk')[:5]
    try:
        custom_range, series = paginate_movies(request, series, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added_series})
    context = {'movies': series,
               'last_added': last_added_series,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def category_cartoon(request):
    """Вывод всех мультфильмов"""
    cartoon = Movie.objects.filter(category=3)
    last_added_cartoon = Movie.objects.filter(category=3).order_by('-pk')[:5]
    try:
        custom_range, cartoon = paginate_movies(request, cartoon, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added_cartoon})
    context = {'movies': cartoon,
               'last_added': last_added_cartoon,
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_red(request):
    """Вывод всех фильмов с низким рейтингом"""
    movie_obj = Movie.objects.all()
    movies = list()
    for i in movie_obj:
        if i.vote_ratio < 5:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_grey(request):
    """Вывод всех фильмов со средним рейтингом"""
    movie_obj = Movie.objects.all()
    movies = list()
    for i in movie_obj:
        if 4.9 < i.vote_ratio < 7:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def rating_movies_green(request):
    """Вывод всех фильмов с высшим рейтингом"""
    movie_obj = Movie.objects.all()
    movies = list()
    for i in movie_obj:
        if 6.9 < i.vote_ratio <= 10:
            movies.append(i)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range
               }
    return render(request, 'home/index.html', context)


def checkbox_search_genre(request):
    """Вывод фильмов отмеченными по жанру"""
    movies, genre = selection_data_genres(request)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range,
               'genre': genre
               }
    return render(request, 'home/index.html', context)


def checkbox_search_year(request):
    """Вывод фильмов отмеченными по годам"""
    movies, year = selection_data_year(request)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'home/index.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range,
               'year': year
               }
    return render(request, 'home/index.html', context)


def actor_detail(request, slug):
    """Вывод полной информации об актёре"""
    actor = Actor.objects.get(name=slug)
    context = {
        'actor': actor,
        'last_added': last_added(),
    }
    return render(request, 'home/actor.html', context)

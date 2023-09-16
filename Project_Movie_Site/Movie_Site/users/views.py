from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage
from home.utils import paginate_movies, last_added
from .utils import user_movies, is_there_review_movie, is_there_review_news, is_there_questions, \
    is_there_questions_review
from home.models import Movie, Review
from news.models import ReviewNews
from forum.models import QuestionUser, ReviewQuestion
from django.db.models import Q


def login_user(request):
    """Авторизация пользователя"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Имя пользователя не существует")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"Вы вошли как '{request.user.username}'")
            return redirect('home')
        else:
            messages.error(request, "Имя пользователя или пароль неверны")
    return render(request, 'users/login_registr.html')


def logout_user(request):
    """Выход из аккаунта"""
    user = request.user.username
    logout(request)
    messages.info(request, f"Вы вышли из аккаунта '{user}'")
    return redirect('login')


def registration(request):
    """Регистрация пользователя"""
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, f"Пользователь '{user.username}' успешно создан!")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, form.errors)

    contex = {'page': page, 'form': form}
    return render(request, 'users/login_registr.html', contex)


@login_required(login_url='login')
def added(request):
    """Добавленные фильмы в раздел 'Мои фильмы'"""
    movies = user_movies(request)
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'users/added.html', {'error': 'Ничего не добавлено', 'last_added': last_added()})
    contex = {'movies': movies,
              'last_added': last_added(),
              'custom_range': custom_range
              }
    return render(request, 'users/added.html', contex)


@login_required(login_url='login')
def search_adding_movie(request):
    """Поиск добавленных фильмов (по названию, английскому названию, по режиссёрам и актёрам) в разделе 'Мои фильмы'"""
    movies = Movie.objects.filter(adding_movie=request.user.id)
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    url_search_query = f"search_query={search_query}&"
    movies = movies.distinct().filter(Q(title__iregex=search_query) |
                                      Q(eng_title__iregex=search_query) |
                                      Q(directors__name__iregex=search_query) |
                                      Q(actors__name__iregex=search_query))
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'users/added.html', {'error': 'Ничего не найдено', 'last_added': last_added()})
    context = {'movies': movies,
               'last_added': last_added(),
               'custom_range': custom_range,
               'search': url_search_query
               }
    return render(request, 'users/added.html', context)


@login_required(login_url='login')
def add_movie(request, slug):
    """Добавление фильма в раздел 'Мои фильмы'"""
    movie_single = Movie.objects.get(url=slug)
    if request.method == "POST":
        movie_single.adding_movie.add(request.user.id)
        movie_single.save()
        messages.success(request, f"Добавлен в раздел 'Мои фильмы'")
        return redirect(movie_single.get_absolute_url())


@login_required(login_url='login')
def deleting_added(request, slug):
    """Удаление фильма из раздела 'Мои фильмы'"""
    movie_single = Movie.objects.get(url=slug)
    if request.method == "POST":
        movie_single.adding_movie.remove(request.user.id)
        messages.error(request, f"Удален из раздела 'Мои фильмы'")
        return redirect(movie_single.get_absolute_url())


@login_required(login_url='login')
def account_settings(request):
    """Настройки аккаунта"""
    review = Review.objects.all()
    review_news = ReviewNews.objects.all()
    forum_question = QuestionUser.objects.all()
    forum_question_review = ReviewQuestion.objects.all()
    availability = is_there_review_movie(request)
    availability_news = is_there_review_news(request)
    availability_question = is_there_questions(request)
    availability_question_review = is_there_questions_review(request)

    contex = {'last_added': last_added(),
              'review': review,
              'review_news': review_news,
              'forum_question': forum_question,
              'forum_question_review': forum_question_review,
              'availability': availability,
              'availability_news': availability_news,
              'availability_question': availability_question,
              'availability_question_review': availability_question_review,
              }
    return render(request, 'users/account_settings.html', contex)


@login_required(login_url='login')
def account_delete(request):
    """Удаление аккаунта"""
    if request.method == "POST":
        user = request.user.username
        User.objects.filter(username=request.user.username).delete()
        messages.success(request, f"Аккаунт '{user}' успешно удален!")
        return redirect('home')


@login_required(login_url='login')
def review_delete(request, slug):
    """Удаление отзыва к фильму"""
    if request.method == "POST":
        movie = Movie.objects.get(url=slug)
        Review.objects.filter(movie_id=movie.id, owner_id=request.user.id).delete()
        messages.success(request, f"Комментарии пользователя {request.user.username} успешно удален!")
        return redirect('account-settings')


@login_required(login_url='login')
def news_review_delete(request, pk):
    """Удаление отзыва к новости"""
    if request.method == "POST":
        ReviewNews.objects.get(id=pk).delete()
        messages.success(request, f"Комментарии пользователя {request.user.username} успешно удален!")
        return redirect('account-settings')


@login_required(login_url='login')
def forum_question_delete(request, pk):
    """Удаление вопроса из форума"""
    if request.method == "POST":
        QuestionUser.objects.get(id=pk).delete()
        messages.success(request, f"Вопрос пользователя {request.user.username} успешно удален!")
        return redirect('account-settings')


@login_required(login_url='login')
def forum_review_question_delete(request, pk):
    """Удаление отзыва к вопросу на форуме"""
    if request.method == "POST":
        ReviewQuestion.objects.get(id=pk).delete()
        messages.success(request, f"Комментарии пользователя {request.user.username} успешно удален!")
        return redirect('account-settings')

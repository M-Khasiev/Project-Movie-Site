from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage
from home.utils import paginate_movies
from .utils import user_movies
from home.models import Movie


def login_user(request):
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
            return redirect('home')
        else:
            messages.error(request, "Имя пользователя или пароль неверны")
    return render(request, 'users/login_registr.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def registration(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Пользователь успешно создан!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'При регистрации произошла ошибка!')

    contex = {'page': page, 'form': form}
    return render(request, 'users/login_registr.html', contex)


@login_required(login_url='login')
def added(request):
    movies = user_movies(request)
    last_added = Movie.objects.order_by('-pk')[:5]
    try:
        custom_range, movies = paginate_movies(request, movies, 6)
    except EmptyPage:
        return render(request, 'users/added.html', {'error': 'Ничего не добавлено', 'last_added': last_added})
    contex = {'movies': movies,
              'last_added': last_added,
              'custom_range': custom_range
              }
    return render(request, 'users/added.html', contex)


def add_movie(request, slug):
    movie_single = Movie.objects.get(url=slug)
    if request.method == "POST":
        movie_single.adding_movie.add(request.user.id)
        movie_single.save()
        messages.success(request, f"Добавлен в 'Мои фильмы'")
        return redirect(movie_single.get_absolute_url())


def deleting_added(request, slug):
    movie_single = Movie.objects.get(url=slug)
    if request.method == "POST":
        movie_single.adding_movie.remove(request.user.id)
        messages.success(request, f"Удален из 'Мои фильмы'")
        return redirect(movie_single.get_absolute_url())

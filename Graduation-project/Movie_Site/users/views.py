from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

menu = [
    {'title': 'Главная', 'url_name': 'home'},
]


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
    contex = {'menu': menu}
    return render(request, 'users/login_registr.html', contex)


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
            messages.error(request, 'При регистрации произошла ошибка')

    contex = {'page': page, 'menu': menu, 'form': form}
    return render(request, 'users/login_registr.html', contex)


@login_required(login_url='login')
def added(request):
    contex = {'menu': menu}
    return render(request, 'users/added.html', contex)

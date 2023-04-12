from django.shortcuts import render, redirect

menu = [
    {'title': 'Главная', 'url_name': 'home'},
]


def home(request):
    contex = {'menu': menu}
    return render(request, 'home/index.html', contex)


def login(request):
    contex = {'menu': menu}
    return render(request, 'home/login.html', contex)


def logout(request):
    ...


def registration(request):
    contex = {'menu': menu}
    return render(request, 'home/registration.html', contex)

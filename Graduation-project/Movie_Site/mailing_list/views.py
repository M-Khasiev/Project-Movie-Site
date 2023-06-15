from django.shortcuts import render, redirect
from .forms import MailingListForm
from django.contrib import messages


def email_save(request):
    if request.method == "POST":
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Email успешно отправлен! Вы подписались на рассылку.')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка или такой email уже существует!')
            return redirect('home')


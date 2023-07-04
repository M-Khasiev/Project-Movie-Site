from django.shortcuts import redirect
from .forms import MailingListForm
from django.contrib import messages


def email_save(request):
    """Сохранение почты для рассылки"""
    if request.method == "POST":
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Email успешно отправлен! Вы подписались на рассылку.')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
            return redirect(request.META.get('HTTP_REFERER'))


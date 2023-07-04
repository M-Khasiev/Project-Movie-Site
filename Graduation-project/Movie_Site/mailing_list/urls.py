from django.urls import path
from . import views

urlpatterns = [
    # Сохранение почты для рассылки
    path("", views.email_save, name='email_save')
]

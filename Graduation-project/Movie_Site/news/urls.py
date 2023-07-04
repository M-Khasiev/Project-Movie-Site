from django.urls import path
from . import views

urlpatterns = [
    # Новости
    path('', views.news, name='news'),
    # Полное описание новости
    path('details-new/<int:pk>/', views.detail_new, name='detail-new'),
]
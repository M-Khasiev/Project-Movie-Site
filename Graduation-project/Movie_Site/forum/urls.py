from django.urls import path
from . import views

urlpatterns = [
    # Форум
    path('', views.forum, name='forum'),
    # Создание вопроса
    path('ask-question/', views.forum_ask_question, name='ask-question'),
    # Добавление вопроса в БД
    path('save-question/', views.save_question, name='save-question'),
    # Поиск вопроса
    path('search-question/', views.search_question, name='search-question'),
    # Детальное описание вопроса
    path('detail-question/<int:pk>/', views.detail_question, name='detail-question'),
]

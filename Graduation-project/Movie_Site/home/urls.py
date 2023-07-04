from django.urls import path
from . import views

urlpatterns = [
    # Главная
    path('', views.home, name='home'),
    # Категория - фильмы
    path('category-movies/', views.category_movies, name='category-movies'),
    # Категория - сериалы
    path('category-series/', views.category_series, name='category-series'),
    # Категория - мультфильмы
    path('category-cartoon/', views.category_cartoon, name='category-cartoon'),
    # Низкий уровень рейтинга
    path('rating-movies-red/', views.rating_movies_red, name='rating-movies-red'),
    # Средний уровень рейтинга
    path('rating-movies-grey/', views.rating_movies_grey, name='rating-movies-grey'),
    # Высокий уровень рейтинга
    path('rating-movies-green/', views.rating_movies_green, name='rating-movies-green'),
    # Поиск по жанрам
    path('checkbox-search-genre/', views.checkbox_search_genre, name='checkbox-search-genre'),
    # Поиск по годам
    path('checkbox-search-year/', views.checkbox_search_year, name='checkbox-search-year'),
    # Поиск фильмов
    path('search-movie/', views.search_movie, name='search-movie'),
    # Детальное описание актёра
    path('actor/<str:slug>/', views.actor_detail, name='actor_detail'),
    # Детальное описание фильма
    path('movie/<slug:slug>/', views.get_movie, name='get-movie'),
]

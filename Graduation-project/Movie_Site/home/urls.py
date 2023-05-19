from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category-movies/', views.category_movies, name='category-movies'),
    path('category-series/', views.category_series, name='category-series'),
    path('category-cartoon/', views.category_cartoon, name='category-cartoon'),
    path('rating-movies-red/', views.rating_movies_red, name='rating-movies-red'),
    path('rating-movies-grey/', views.rating_movies_grey, name='rating-movies-grey'),
    path('rating-movies-green/', views.rating_movies_green, name='rating-movies-green'),
    path('checkbox-search-genre/', views.checkbox_search_genre, name='checkbox-search-genre'),
    path('checkbox-search-year/', views.checkbox_search_year, name='checkbox-search-year'),
    path('search-movie/', views.search_movie, name='search-movie'),
    path('actor/<str:slug>/', views.actor_detail, name='actor_detail'),
    path('movie/<slug:slug>/', views.get_movie, name='get-movie'),
]
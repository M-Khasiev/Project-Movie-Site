from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>/', views.get_movie, name='get-movie'),
    path('category-movies/', views.category_movies, name='category-movies'),
    path('category-series/', views.category_series, name='category-series'),
    path('category-cartoon/', views.category_cartoon, name='category-cartoon'),
]
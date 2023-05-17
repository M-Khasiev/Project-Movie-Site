from django.contrib import admin
from .models import Movie, Actor, Category, Genre, MovieShots, RatingStar, Rating, Review

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)


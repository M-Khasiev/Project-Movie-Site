from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Movie, Actor, Category, Genre, MovieShots, Review, FactsMovie


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Review
    extra = 1
    readonly_fields = ("owner", "movie", 'created')


class MovieShotsInline(admin.TabularInline):
    """Кадры на странице фильма"""
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="80"')

    get_image.short_description = 'Изображение'


class FactsMovieInline(admin.TabularInline):
    """Факты о фильме"""
    model = FactsMovie
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "eng_title", "created", 'get_image')
    list_filter = ("category", "year")
    search_fields = ("title", "category__name", 'eng_title')
    inlines = [MovieShotsInline, FactsMovieInline, ReviewInline]
    save_on_top = True
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90" height="130"')

    get_image.short_description = 'Постер'


class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age", "get_image")
    search_fields = ("name", "eng_name")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = 'Изображение'


class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie", 'get_image')
    search_fields = ("movie", "movie__eng_title")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="80"')

    get_image.short_description = 'Изображение'


class FactsMovieAdmin(admin.ModelAdmin):
    """Факты о фильме"""
    list_display = ("movie", "description")
    list_display_links = ("movie",)
    search_fields = ("movie__title", "movie__eng_title")


class ReviewAdmin(admin.ModelAdmin):
    """Отзыв и оценка"""
    list_display = ("owner", "value", "movie")
    list_display_links = ("owner", "value")
    search_fields = ("owner__username", "value", "movie__title", "movie__eng_title")


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(FactsMovie, FactsMovieAdmin)

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, ReviewNews


class ReviewNewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = ReviewNews
    extra = 1
    readonly_fields = ("owner", 'created')


class NewsAdmin(admin.ModelAdmin):
    """Новости"""
    list_display = ("title", "get_image", "time")
    list_display_links = ("title", "get_image", "time")
    readonly_fields = ("get_image",)
    inlines = [ReviewNewInline]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.url_image} width="120" height="80"')

    get_image.short_description = 'Изображение'


class ReviewNewsAdmin(admin.ModelAdmin):
    """Отзывы на странице фильма"""
    list_display = ('owner', 'news', 'created')
    list_display_links = ('owner', 'news')
    list_filter = ('owner', 'created')
    search_fields = ('owner__username', 'created')


admin.site.register(News, NewsAdmin)
admin.site.register(ReviewNews, ReviewNewsAdmin)

admin.site.site_title = 'Movie-Site'
admin.site.site_header = 'Movie-Site'

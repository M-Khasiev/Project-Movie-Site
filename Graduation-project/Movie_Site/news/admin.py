from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "get_image", "time")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.url_image} width="120" height="80"')

    get_image.short_description = 'Изображение'


admin.site.register(News, NewsAdmin)

admin.site.site_title = 'Movie-Site'
admin.site.site_header = 'Movie-Site'

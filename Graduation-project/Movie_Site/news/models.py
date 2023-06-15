from django.db import models


class News(models.Model):
    title = models.CharField("Название", max_length=300, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    url_image = models.URLField('Путь к картинке', default='')
    description = models.TextField("Описание")
    newsletter = models.BooleanField('Была отправлен как рассылка', default=False)

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ['-time']

from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    """Новости"""
    title = models.CharField("Название", max_length=300, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    url_image = models.URLField('Путь к картинке', default='')
    description = models.TextField("Описание")
    newsletter = models.BooleanField('Была отправлен как рассылка', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ['-time']


class ReviewNews(models.Model):
    """Отзыв новости"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')
    body = models.TextField(default='', verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.owner.username

    class Meta:
        ordering = ["created"]
        verbose_name = "Отзыв новости"
        verbose_name_plural = "Отзыв новости"

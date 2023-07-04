from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class QuestionUser(models.Model):
    """Вопрос пользователя"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    subject = models.CharField(max_length=200,  default='', verbose_name='Заголовок (обязательное поле)')
    question = RichTextUploadingField(null=True, verbose_name='Раскройте суть вопроса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос из форума"
        verbose_name_plural = "Вопрос из форума"
        ordering = ['-created']


class ReviewQuestion(models.Model):
    """Отзыв к вопросу"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    question_user = models.ForeignKey(QuestionUser, on_delete=models.CASCADE, verbose_name='Вопрос пользователя')
    body = models.TextField(default='', verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.owner.username

    class Meta:
        ordering = ["created"]
        verbose_name = "Отзыв к вопросу"
        verbose_name_plural = "Отзыв к вопросу"

from django.db import models


class MailingList(models.Model):
    """Рассылка на Email"""
    email = models.EmailField('Email', unique=True)
    date = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = "Рассылка на Email"
        verbose_name_plural = "Рассылка на Email"

    def __str__(self):
        return self.email

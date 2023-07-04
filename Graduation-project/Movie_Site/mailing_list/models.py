from django.db import models


class MailingList(models.Model):
    """Рассылка на Email"""
    email = models.EmailField('Email', unique=True)
    date = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Рассылка на Email"
        verbose_name_plural = "Рассылка на Email"

# Generated by Django 4.2.2 on 2023-06-23 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_news_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Новость')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв новости',
                'verbose_name_plural': 'Отзыв новости',
                'ordering': ['-created'],
            },
        ),
    ]
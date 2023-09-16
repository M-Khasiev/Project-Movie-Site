# Generated by Django 4.1.7 on 2023-05-15 19:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_movie_vote_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='adding_movie',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
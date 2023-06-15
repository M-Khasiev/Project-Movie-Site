# Generated by Django 4.1.7 on 2023-06-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_actor_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='Место рождения'),
        ),
        migrations.AddField(
            model_name='actor',
            name='height',
            field=models.FloatField(default=0, verbose_name='Рост'),
        ),
    ]

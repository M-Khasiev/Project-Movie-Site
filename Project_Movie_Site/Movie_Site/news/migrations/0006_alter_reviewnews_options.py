# Generated by Django 4.2.2 on 2023-07-06 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_reviewnews_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewnews',
            options={'ordering': ['created'], 'verbose_name': 'Отзыв новости', 'verbose_name_plural': 'Отзыв новости'},
        ),
    ]
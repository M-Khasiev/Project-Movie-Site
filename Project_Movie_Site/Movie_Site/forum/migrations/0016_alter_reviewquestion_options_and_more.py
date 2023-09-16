# Generated by Django 4.2.2 on 2023-07-09 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_alter_reviewquestion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewquestion',
            options={'ordering': ['created'], 'verbose_name': 'Комментарии к вопросу', 'verbose_name_plural': 'Комментарии к вопросу'},
        ),
        migrations.AlterField(
            model_name='reviewquestion',
            name='body',
            field=models.TextField(default='', verbose_name='Комментарий'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_questionuser_subject_alter_questionuser_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionuser',
            name='question',
            field=models.TextField(blank=True, null=True, verbose_name='Раскройте суть вопроса'),
        ),
    ]
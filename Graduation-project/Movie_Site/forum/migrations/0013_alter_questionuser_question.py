# Generated by Django 4.2.2 on 2023-06-26 17:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_alter_questionuser_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionuser',
            name='question',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Раскройте суть вопроса'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-12 05:37

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Тема поста')),
                ('image', models.ImageField(upload_to='blog_photo', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])], verbose_name='Фото поста')),
                ('description', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
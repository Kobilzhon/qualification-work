# Generated by Django 4.2.1 on 2023-05-13 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='id_blog',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
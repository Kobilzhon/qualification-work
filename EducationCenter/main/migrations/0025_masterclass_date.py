# Generated by Django 4.2.1 on 2023-05-19 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_rename_masterclasses_masterclass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclass',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 3, 16, 28, 962889), null=True),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-06 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 4, 6, 6, 48, 37, 818104, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1 on 2022-11-10 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0023_alter_feed_created_at_alter_feed_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 10, 4, 48, 291632)),
        ),
    ]

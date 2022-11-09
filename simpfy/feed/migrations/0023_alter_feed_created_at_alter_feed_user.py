# Generated by Django 4.1 on 2022-11-08 07:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0008_alter_profile_image'),
        ('feed', '0022_alter_feed_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 15, 23, 20, 45222)),
        ),
        migrations.AlterField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.profile'),
        ),
    ]
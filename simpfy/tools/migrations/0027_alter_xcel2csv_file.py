# Generated by Django 4.1 on 2022-11-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0026_xcel2csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xcel2csv',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='mp3'),
        ),
    ]

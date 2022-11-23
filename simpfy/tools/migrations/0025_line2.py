# Generated by Django 4.1 on 2022-11-17 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0009_alter_profile_saved'),
        ('tools', '0024_scatter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='line2')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prof.profile')),
            ],
        ),
    ]
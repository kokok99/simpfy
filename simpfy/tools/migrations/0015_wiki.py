# Generated by Django 4.1 on 2022-11-14 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0009_alter_profile_saved'),
        ('tools', '0014_rename_output_wolf_outputtext_wolf_outputimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(blank=True, max_length=1000, null=True)),
                ('outputtext', models.TextField(blank=True, max_length=10000, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prof.profile')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20211106_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movies/movies/images'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='movies/movies/videos'),
        ),
    ]

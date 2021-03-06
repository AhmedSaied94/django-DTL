# Generated by Django 3.2.9 on 2021-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Movie Name')),
                ('rated', models.CharField(default='pg-13', max_length=255)),
                ('relased', models.DateField(blank=True, null=True)),
                ('run_time', models.IntegerField(default=0, null=True)),
                ('genre', models.CharField(max_length=255, null=True)),
                ('plot', models.CharField(default='THis Is Film Descripe', max_length=400)),
                ('language', models.CharField(default='English', max_length=255)),
                ('poster', models.ImageField(upload_to='')),
                ('imdp_rate', models.FloatField(default=0, null=True)),
                ('active', models.BooleanField(default=True)),
                ('likes', models.IntegerField(default=0, null=True)),
                ('watch_count', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]

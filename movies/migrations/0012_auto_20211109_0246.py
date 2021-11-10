# Generated by Django 3.2.9 on 2021-11-09 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_cast_ssn_movie_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='ssn',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.cast_ssn'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='serial',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie_serial'),
            preserve_default=False,
        ),
    ]
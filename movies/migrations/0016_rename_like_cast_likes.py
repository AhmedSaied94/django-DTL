# Generated by Django 3.2.9 on 2021-11-09 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_cast_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast',
            old_name='like',
            new_name='likes',
        ),
    ]

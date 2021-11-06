from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class movies(models.Model):
    title = models.CharField("Movie Name", unique=True, max_length=255)
    rated = models.CharField(default="pg-13", max_length=255)
    relased = models.DateField(blank=True, null=True)
    run_time = models.IntegerField(default=0, null=True)
    genre = models.CharField(null=True, max_length=255)
    plot = models.CharField(default="THis Is Film Descripe",max_length=400)
    language = models.CharField(default="English", max_length=255)
    poster = models.ImageField(null=True,upload_to='movies/images')
    video = models.FileField(null=True,upload_to='movies/videos')
    imdp_rate = models.FloatField(default=0, null=True)
    active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0, null=True)
    watch_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class cast(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    job = models.CharField(default="Actor",max_length=255)
    nationality = models.CharField(null=True,max_length=255)
    known_for = models.CharField(null=True,max_length=255)
    profile_pic = models.ImageField(null=True,upload_to='actors/images')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
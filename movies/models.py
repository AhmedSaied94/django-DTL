from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField
from datetime import date
from django.utils import timezone


# Create your models here.

class movies(models.Model):
    title = models.CharField("Movie Name", unique=True, max_length=255)
    rated = models.CharField(default="pg-13", max_length=255)
    relased = models.DateField(blank=True, null=True)
    run_time = models.IntegerField(default=0, null=True)
    genre = models.CharField(null=True, max_length=255)
    plot = models.CharField(default="THis Is Film Descripe",max_length=400)
    language = models.CharField(default="English", max_length=255)
    poster = models.ImageField(null=True,blank=True,upload_to='movies/movies/images')
    video = models.FileField(null=True,blank=True,upload_to='movies/movies/videos')
    imdp_rate = models.FloatField(default=0, null=True)
    active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0, null=True)
    watch_count = models.IntegerField(default=0, null=True)
    cast = models.ManyToManyField("cast")
    serial = models.OneToOneField("movies_serial", on_delete=CASCADE)
    class Meta:
        verbose_name_plural = "Movies"
        ordering = ["-imdp_rate"]

    def __str__(self):
        return self.title


class cast(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    job = models.CharField(default="Actor",max_length=255)
    likes= models.IntegerField(default=0, null=True)
    nationality = models.CharField(null=True,max_length=255)
    known_for = models.CharField(null=True,max_length=255)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='movies/cast/images')
    ssn = models.OneToOneField("cast_ssn", on_delete=CASCADE)
    
    class Meta:
        ordering = ["age"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date = models.DateField(default=timezone.now)
    
    class Meta:
        abstract = True
    


class movies_comment(comments):
    attachment = models.ImageField(null=True, blank=True, upload_to="movies/attachment/movies")
    movie = models.ForeignKey("movies", on_delete=CASCADE, null=True)

    def __str__(self):
        return self.movie.title



class cast_comment(comments):
    attachment = models.ImageField(null=True, blank=True, upload_to="movies/attachment/cast")
    cast = models.ForeignKey("cast", on_delete=CASCADE)

    def __str__(self):
        return self.cast.name

class movies_serial(models.Model):
    serial = models.CharField(max_length=50)

    def __str__(self):
        return f"NO: {self.serial}"

class cast_ssn(models.Model):
    ssn = models.IntegerField()

    def __str__(self):
        return f"NO: {self.ssn}"

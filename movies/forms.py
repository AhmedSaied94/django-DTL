from django.db import models
from django.forms import ModelForm
from .models import movies, cast, movies_comment, cast_comment

class movies_form(ModelForm):
    class Meta:
        model = movies
        fields = '__all__'

class cast_form(ModelForm):
    class Meta:
        model = cast
        fields = '__all__'
        
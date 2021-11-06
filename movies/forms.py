from django.forms import ModelForm
from .models import movies

class movies_form(ModelForm):
    class Meta:
        model = movies
        fields = '__all__'

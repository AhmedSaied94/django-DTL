from typing import cast
from django.contrib import admin
from .models import *

admin.site.register(movies)
admin.site.register(cast)

# Register your models here.

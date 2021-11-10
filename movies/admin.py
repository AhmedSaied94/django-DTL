from typing import cast
from django.contrib import admin
from .models import *

admin.site.register(movies)
admin.site.register(cast)
admin.site.register(movies_comment)
admin.site.register(cast_comment)
admin.site.register(cast_ssn)
admin.site.register(movies_serial)

# Register your models here.

from typing import cast
from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *

class comment_inline(admin.StackedInline):
    model = movies_comment
    extra = 2


class moviesAdmin(admin.ModelAdmin):
    list_filter = ('imdp_rate', 'likes')
    search_fields = ('title','cast__first_name')
    list_display = ('title', 'imdp_rate', 'genre', 'likes', 'like_to_watch')
    readonly_fields = ['like_to_watch', 'watch_count']
    inlines = [comment_inline]

    def like_to_watch(self, obj):
        if not obj.watch_count or not obj.likes:
            return 0
        else:
            return f"{round(obj.likes/obj.watch_count, 2)*100}%"
    like_to_watch.short_description = 'Like watch %'
    


    fieldsets = (
        ['About', {'fields':['title', 'plot', 'genre', 'rated', 'language']}],
        ['Numbers', {'fields':['relased', 'run_time', 'serial']}],
        ['Statue', {'fields':['likes', 'watch_count', 'like_to_watch', 'imdp_rate', 'active']}],
        ['Data', {'fields':['poster', 'video', 'cast']}]
    )


# Register your models here.

admin.site.register(movies, moviesAdmin)
admin.site.register(cast)
admin.site.register(movies_comment)
admin.site.register(cast_comment)
admin.site.register(cast_ssn)
admin.site.register(movies_serial)




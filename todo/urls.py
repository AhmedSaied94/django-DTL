from django.urls import path
from django.urls.resolvers import URLPattern
from .views import to_watch_list, to_watch_delete, to_watch_details, to_watch_list, to_watch_update

app_name = "todo"

urlpatterns = [
    path("", to_watch_list, name="to-watch-list"),
    path("movie/<str:movie_id>/details", to_watch_details, name="to-watch-details"),
    path("movie/<str:movie_id>/update", to_watch_update, name="to-watch-update"),
    path("movie/<movie_id>/delete", to_watch_delete, name="to-watch-delete")
    
]
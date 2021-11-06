

from django.urls.conf import path
from .views import *

app_name = "movies"

urlpatterns = [
    path("", home, name="home"),
    path("movies-list", movies_list, name="movies-list"),
    path("movies/<int:pk>/update", update_movie, name="update-movie"),
    path('movies/<int:pk>/details', movie_details, name="movie-details"),
    path("movies/<int:pk>/delete", delete_movie, name="delete-movie"),
    path("movies/add", add_movie, name="add-movie")
]
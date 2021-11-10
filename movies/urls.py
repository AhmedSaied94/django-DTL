

from django.urls.conf import path
from .views import *

app_name = "movies"

urlpatterns = [
    path("", home, name="home"),
    path("movies-list", movies_list, name="movies-list"),
    path("movies/<int:pk>/update", update_movie, name="update-movie"),
    path('movies/<int:pk>/details', movie_details, name="movie-details"),
    path("movies/<int:pk>/delete", delete_movie, name="delete-movie"),
    path("movies/add", add_movie, name="add-movie"),
    path("cast-lis", cast_list, name="cast-list"),
    path("cast/add", cast_add, name="add-cast"),
    path("cast/<int:pk>/update", cast_update, name="update-cast"),
    path("cast/<int:pk>/details", cast_details, name="cast-details"),
    path("cast/<int:pk>/delete", cast_delete, name="delete-cast"),
    path("comment/<int:mpk>/<int:cpk>/<str:cls>/delete", comment_delete, name="comment-delete"),
    path("<str:cls>/<str:pk>/like", btn_like, name="like")
]
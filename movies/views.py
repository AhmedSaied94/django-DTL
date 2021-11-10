from django.http import request
from django.shortcuts import redirect, render 
from .models import movies , cast, movies_comment, cast_comment
from .forms import movies_form, cast_form


# Create your views here.

def home(request):
    return render(request, "movies/home.html")

def movie_details(request, pk):
    movie = movies.objects.get(id=pk)
    if request.method == "POST":
        c_text = request.POST.get('text')
        C_attachment = request.POST.get('attachment')
        movies_comment.objects.create(text=c_text, user=request.user, attachment=C_attachment, movie=movie)
        return redirect("movies:movie-details", pk=movie.id)

    else:
        return render(request, "movies/movie_details.html", context={"movie":movie})

def movies_list(request):
    all_movies = movies.objects.all()
    return render(request, "movies/movies_list.html", context={"all_movies":all_movies})

def add_movie(request):
    form = movies_form()
    if request.method == "POST":
        form = movies_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movies:movies-list")
    return render(request, "movies/add_movie.html", context={"form":form})

def update_movie(request, pk):
    movie = movies.objects.get(id=pk)
    form = movies_form(instance=movie)
    if request.method == 'POST':
        form = movies_form(data=request.POST,files=request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:movie-details", pk=movie.id)
    return render(request, "movies/update_movie.html", context={"form":form, "movie":movie})

def delete_movie(request, pk):
    movies.objects.get(id=pk).delete()
    return redirect("movies:movies-list")


def cast_add(request):
    form = cast_form
    if request.method == "POST":
        form = cast_form(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect("movies:cast-list")
    return render(request, "movies/add_cast.html", context={"form":form})

def cast_update(request, pk):
    u_cast = cast.objects.get(id=pk)
    form = cast_form(instance=u_cast)
    if request.method == "POST":
        form = cast_form(data=request.POST, files=request.FILES, instance=u_cast)
        if form.is_valid():
            form.save()
            return redirect("movies:cast-details")
    return render(request, "movies/cast_update.html", context={"form":form, "cast":u_cast})

def cast_details(request, pk):
    u_cast = cast.objects.get(id=pk)
    if request.method == "POST":
        c_text = request.POST.get('text')
        C_attachment = request.POST.get('attachment')
        cast_comment.objects.create(text=c_text, user=request.user, attachment=C_attachment, cast=u_cast)
        return redirect("movies:cast-details", pk=u_cast.id)
    else:
        return render(request, "movies/cast_details.html", context={"cast":u_cast})

def cast_delete(request, pk):
    cast.objects.get(id=pk).delete()
    return redirect("movies:cast-list")

def cast_list(request):
    cast_li = cast.objects.all()
    return render(request, "movies/cast_list.html", context={"cast":cast_li})

def comment_delete(request, mpk, cpk, cls):
    if cls == "movies":
        movies_comment.objects.get(id=cpk).delete()
        return redirect("movies:movie-details", pk=mpk)
    else:
        cast_comment.objects.get(id=cpk).delete()
        return redirect("movies:cast-details", pk=mpk)

def btn_like(request, cls, pk):
    if cls == "movies":
        movie = movies.objects.get(id=pk)
        movies.objects.filter(id=pk).update(likes=movie.likes+1)
        return redirect("movies:movie-details", pk=pk)
    else:
        u_cast = cast.objects.get(id=pk)
        cast.objects.filter(id=pk).update(likes=u_cast.likes+1)
        return redirect("movies:cast-details", pk=pk)
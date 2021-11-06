from django.shortcuts import redirect, render 
from .models import movies
from .forms import movies_form

# Create your views here.

def home(request):
    return render(request, "movies/home.html")

def movie_details(request, pk):
    movie = movies.objects.get(id=pk)
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
        form = movies_form(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:movie-details", pk=movie.id)
    return render(request, "movies/update_movie.html", context={"form":form, "movie":movie})

def delete_movie(request, pk):
    movies.objects.get(id=pk).delete()
    return redirect("movies:movies-list")
from django.shortcuts import render
import pip._vendor.requests 



movies_list = [
    pip._vendor.requests.get("http://www.omdbapi.com/?t=free+guy&y=2021&plot=short&r=json&apikey=bd3ad5ed").json(),
    pip._vendor.requests.get("http://www.omdbapi.com/?t=shang+chi&y=2021&plot=short&r=json&apikey=bd3ad5ed").json(),
    pip._vendor.requests.get("http://www.omdbapi.com/?t=black+widow&y=2021&plot=short&r=json&apikey=bd3ad5ed").json(),
    pip._vendor.requests.get("http://www.omdbapi.com/?t=eternals&y=2021&plot=short&r=json&apikey=bd3ad5ed").json(),
    pip._vendor.requests.get("http://www.omdbapi.com/?t=batman&y=2021&plot=short&r=json&apikey=bd3ad5ed").json(),
    pip._vendor.requests.get("http://www.omdbapi.com/?t=venom&y=2021&plot=short&r=json&apikey=bd3ad5ed").json()
]


tasks_list = [
    {
        "id":1,
        "index":0,
        "name":"task #1",
        "priority":4,
        "discription":"this is task number one #1"
    },
    {
        "id":3,
        "index":2,
        "name":"task #3",
        "priority":3,
        "discription":"this is task number one #3"
    },
    {
        "id":4,
        "index":3,
        "name":"task #3",
        "priority":5,
        "discription":"this is task number one #4"
    },
    {
        "id":5,
        "index":4,
        "name":"task #5",
        "priority":1,
        "discription":"this is task number one #5"
    },
    {
        "id":6,
        "index":5,
        "name":"task #6",
        "priority":7,
        "discription":"this is task number one #6"
    }
]

# def get_task(task_id):
#     result = list(filter(lambda item:item.get("id") == task_id, tasks_list))
#     task_index = tasks_list.index(result[0])
#     return task_index

def get_movie(movie_id):
    result = list(filter(lambda item:item.get("imdbID") == movie_id, movies_list))
    movie_index = movies_list.index(result[0])
    return movie_index

# def todo_details(request, **kwargs):
#     task_index = get_task(kwargs.get("task_id"))
#     task = tasks_list[task_index]
#     return render(request, "todo/todo_details.html", context=task)

def to_watch_details(request, **kwargs):
    movie_index = get_movie(kwargs.get("movie_id"))
    movie = movies_list[movie_index]
    return render(request, "todo/movie_details.html", context=movie)
    

# def todo_update(request, **kwargs):
#     task_index = get_task(kwargs.get("task_id"))
#     task_name = tasks_list[task_index]["name"]
#     tasks_list[task_index]["name"] = f"Updated {task_name}"
#     return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})

def to_watch_update(request, **kwargs):
    movie_index = get_movie(kwargs.get("movie_id"))
    movie_title = movies_list[movie_index]["Title"]
    movies_list[movie_index]["Title"] = f"Watched {movie_title}"
    return render(request, "todo/to_watch_list.html", context={"movies_list":movies_list})
    


# def todo_delete(request, **kwargs):
#     task_index = get_task(kwargs.get("task_id"))
#     task = tasks_list[task_index]
#     tasks_list.remove(task)
#     return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})

def to_watch_delete(request, **kwargs):
    movie_index = get_movie(kwargs.get("movie_id"))
    movie = movies_list[movie_index]
    movies_list.remove(movie)
    return render(request, "todo/to_watch_list.html", context={"movies_list":movies_list})
   
    
    
# def todo_list(request):

#     return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})

def to_watch_list(request):

    return render(request, "todo/to_watch_list.html", context={"movies_list":movies_list})

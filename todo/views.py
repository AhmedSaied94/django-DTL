from django.shortcuts import render

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

def get_task(task_id):
    result = list(filter(lambda item:item.get("id") == task_id, tasks_list))
    task_index = tasks_list.index(result[0])
    return task_index

def todo_details(request, **kwargs):
    task_index = get_task(kwargs.get("task_id"))
    task = tasks_list[task_index]
    return render(request, "todo/todo_details.html", context=task)
    

def todo_update(request, **kwargs):
    task_index = get_task(kwargs.get("task_id"))
    task_name = tasks_list[task_index]["name"]
    tasks_list[task_index]["name"] = f"Updated {task_name}"
    return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})
    


def todo_delete(request, **kwargs):
    task_index = get_task(kwargs.get("task_id"))
    task = tasks_list[task_index]
    tasks_list.remove(task)
    return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})
   
    
    
def todo_list(request):

    return render(request, "todo/todo_list.html", context={"tasks_list":tasks_list})

from django.urls import path
from django.urls.resolvers import URLPattern
from .views import todo_delete, todo_details, todo_list, todo_update

app_name = "todo"

urlpatterns = [
    path("", todo_list, name="todo-list"),
    path("task/<int:task_id>/details", todo_details, name="todo-details"),
    path("task/<int:task_id>/update", todo_update, name="todo-update"),
    path("task/<int:task_id>/delete", todo_delete, name="todo-delete")
    
]
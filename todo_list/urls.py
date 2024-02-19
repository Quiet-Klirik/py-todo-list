from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("task-create", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
]

app_name = "todo_list"

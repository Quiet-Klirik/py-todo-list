from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo:list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo:list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:list")


class TaskSwitchView(generic.View):
    model = Task
    object = None

    def get_object(self):
        if not self.object:
            pk = self.kwargs["pk"]
            self.object = self.model.objects.get(pk=pk)
        return self.object

    def get(self, *args, **kwargs):
        object = self.get_object()
        if object.is_done:
            object.is_done = False
        else:
            object.is_done = True
        object.save()
        return redirect("todo:list")

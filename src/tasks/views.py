from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')


def toggle_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from tasks.models import Task
from tasks.forms import TaskForm


#https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/
# https://docs.djangoproject.com/en/5.0/intro/tutorial03/
# https://bootstrap-5.ru/docs/5.3/forms/input-group/
# https://bootstrap5.ru/docs/formy/form-control
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks/task-list')
    template_name = 'tasks/task_delete.html'   #task_confirm_delete - можно переименовать


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    # fields = ['title', 'description', 'execution_status', 'due_date']
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy('task_list')


class TaskCreateView(CreateView):
    model = Task
    # fields = ['title', 'description', 'execution_status', 'due_date']
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'



# from django.http import HttpResponse
# from django.shortcuts import render

# def base_site(request):
#     return render(request, 'base_site.html')
#
#
# def TaskListView(ListView):
#     return render(request, 'tasks/task_list.html')
#
#
# def create_task(request):
#     return render(request, 'tasks/task.html')
#
#
# def task_detail(request):
#     return render(request, 'tasks/task.html')
#
# def delete_task(request):
#     return render(request, 'tasks/task.html')

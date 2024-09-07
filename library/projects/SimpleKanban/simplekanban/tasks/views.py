from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from tasks.models import Task
from tasks.forms import TaskForm


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    # template_name = 'tasks/task_list.html'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks/task-list')
    template_name = 'tasks/task_delete.html'


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy('task_list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'




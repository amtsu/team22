
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import TaskForm, WorkGroupForm, SubTaskFormSet
from .models import Task, SubTask, WorkGroup


def home_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request, 'account/home.html')


# Представление для просмотра списка Задач
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    # template_name = 'tasks/task_list.html'


# Представление для удаления Задачи
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks/task-list')
    template_name = 'tasks/task_delete.html'


# Представление для детальной информации о Задаче
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем все подзадачи:
        context['subtasks'] = self.object.subtasks.all()
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['subtasks'] = SubTaskFormSet(self.request.POST)
        else:
            context['subtasks'] = SubTaskFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']
        form.instance.author = self.request.user

        if form.is_valid() and subtasks.is_valid():
            # Сохраняем задачу
            response = super().form_valid(form)

            # Привязываем подзадачи к сохраненной задаче
            subtasks.instance = self.object
            subtasks.save()

            return response
        return self.form_invalid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['subtasks'] = SubTaskFormSet(self.request.POST, instance=self.object)
        else:
            data['subtasks'] = SubTaskFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']

        if form.is_valid() and subtasks.is_valid():
            response = super().form_valid(form)
            subtasks.instance = self.object
            subtasks.save()
            return response
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        # self.object.id для получения идентификатора задачи
        return reverse_lazy('task_detail', kwargs={'pk': self.object.id})


# Представление для создания Рабочей Группы
class WorkGroupCreateView(CreateView):
    model = WorkGroup
    form_class = WorkGroupForm
    template_name = 'workgroups/workgroup_form.html'
    success_url = reverse_lazy('workgroup_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем текущего пользователя как владельца
        return super().form_valid(form)


# Представление для редактирования Рабочей Группы
class WorkGroupUpdateView(UpdateView):
    model = WorkGroup
    form_class = WorkGroupForm
    template_name = 'workgroups/workgroup_form.html'
    success_url = reverse_lazy('workgroup_list')

    def form_valid(self, form):
        return super().form_valid(form)


# Представление для удаления Рабочей Группы
class WorkGroupDeleteView(DeleteView):
    model = WorkGroup
    template_name = 'workgroups/workgroup_confirm_delete.html'  # Путь к шаблону
    success_url = reverse_lazy('workgroup_list')


# Представление для просмотра списка Рабочих Групп
class WorkGroupListView(ListView):
    model = WorkGroup
    context_object_name = 'workgroups'  # Это имя будет доступно в шаблоне
    template_name = 'workgroups/workgroup_list.html'  # Путь к шаблону

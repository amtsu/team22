
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import TaskForm, SubTaskFormSet, CompanyForm
from .models import Task, Company


# Представление для просмотра списка компаний
class CompanyListView(ListView):
    model = Company
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'  # Имя переменной, доступной в шаблоне

    def get_queryset(self):
        return Company.objects.all()  # Возвращает все объекты компании


# Представление для создания компании
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_create.html'
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем текущего пользователя как владельца
        return super().form_valid(form)


# Представление для детальной информации о компании
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'


def home_view(request):
    if request.user.is_authenticated:
        return redirect('task_list_all')
    return render(request, 'account/home.html')


# Представление для просмотра списка Задач
class TaskListView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.request.GET.get('company_id')

        if company_id:
            context['tasks'] = context['tasks'].filter(company_id=company_id)
            context['selected_company'] = get_object_or_404(Company, id=company_id)

        context['companies'] = Company.objects.all()  # Отправляем все компании для возможной фильтрации
        return context


# Представление для удаления Задачи
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')  # Убедитесь, что у вас правильно настроен success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.object.company  # Предполагается, что у задачи есть поле company
        context['company'] = company if company else None
        return context


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
    context_object_name = 'task_create'
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

        # Связываем задачу с компанией, если это необходимо
        company_id = self.kwargs.get('company_id')
        if company_id:
            form.instance.company = get_object_or_404(Company, id=company_id)

        if subtasks.is_valid():
            response = super().form_valid(form)
            subtasks.instance = self.object
            subtasks.save()
            return response
        else:
            return self.form_invalid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    context_object_name = 'task_edit'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['subtasks'] = SubTaskFormSet(self.request.POST, instance=self.object)
        else:
            data['subtasks'] = SubTaskFormSet(instance=self.object)
        return data

    def form_invalid(self, form):
        context = self.get_context_data()
        context['subtasks'] = SubTaskFormSet(self.request.POST, instance=self.object)
        return self.render_to_response(context)

    def get_success_url(self):
        # self.object.id для получения идентификатора задачи
        return reverse_lazy('task_detail', kwargs={'pk': self.object.id})


class TaskListAllView(ListView):
    model = Task
    template_name = 'tasks/task_list_all.html'  # Шаблон для отображения всех задач
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()  # Возвращает все задачи

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.request.GET.get('company_id')
        context['company_id'] = company_id if company_id else None  # Динамически передаем ID компании
        return context

#
# # Представление для создания Рабочей Группы
# class WorkGroupCreateView(CreateView):
#     model = WorkGroup
#     form_class = WorkGroupForm
#     template_name = 'workgroups/workgroup_form.html'
#     success_url = reverse_lazy('workgroup_list')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user  # Устанавливаем текущего пользователя как владельца
#         return super().form_valid(form)
#
#
# # Представление для редактирования Рабочей Группы
# class WorkGroupUpdateView(UpdateView):
#     model = WorkGroup
#     form_class = WorkGroupForm
#     template_name = 'workgroups/workgroup_form.html'
#     success_url = reverse_lazy('workgroup_list')
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#
# # Представление для удаления Рабочей Группы
# class WorkGroupDeleteView(DeleteView):
#     model = WorkGroup
#     template_name = 'workgroups/workgroup_confirm_delete.html'  # Путь к шаблону
#     success_url = reverse_lazy('workgroup_list')
#
#
# # Представление для просмотра списка Рабочих Групп
# class WorkGroupListView(ListView):
#     model = WorkGroup
#     context_object_name = 'workgroups'  # Это имя будет доступно в шаблоне
#     template_name = 'workgroups/workgroup_list.html'  # Путь к шаблону

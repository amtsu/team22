from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import View

from django.core.mail import send_mail
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import TaskForm, SubTaskFormSet, CompanyForm
from .models import Task, Company, SubTask
import json


# Представление для просмотра списка компаний
class CompanyListView(ListView):
    model = Company
    template_name = 'tasks/companies/company_list.html'
    context_object_name = 'companies'  # Имя переменной, доступной в шаблоне

    def get_queryset(self):
        return Company.objects.all()  # Возвращает все объекты компании


class CompanyCreateView(View):

    def get(self, request):
        all_users = User.objects.all()
        form = CompanyForm()
        return render(request, 'tasks/companies/company_create.html', {'form': form, 'all_users': all_users})

    def post(self, request):
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save()

            # Обработка выбранных участников и приглашенных по email
            selected_members = json.loads(request.POST.get('selected_members', '[]'))
            members = []

            for member in selected_members:
                if member['type'] == 'registered':
                    # Если участник выбран из зарегистрированных пользователей
                    user = User.objects.get(id=member['id'])
                    members.append(user)
                elif member['type'] == 'email':
                    # Если участник приглашен по email
                    user, created = User.objects.get_or_create(
                        email=member['email'],
                        defaults={'username': member['email'].split('@')[0]}
                    )
                    members.append(user)

                    if created:
                        # Отправляем приглашение новому пользователю
                        self.send_invitation(company, request.user, member['email'])

            # Заполняем поле members
            company.members.set(members)  # Используем set для множественных пользователей

            return redirect('company_list')  # Перенаправление на список компаний
        else:
            print(form.errors)  # Для отладки
            all_users = User.objects.all()
            return render(request, 'tasks/companies/company_create.html', {'form': form, 'all_users': all_users})

    def send_invitation(self, company, sender, email):
        """Функция для отправки приглашения по email."""
        subject = f'Приглашение присоединиться к компании {company.name}'
        message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
        send_mail(subject, message, sender.email, [email])


class CompanyEditView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        all_users = User.objects.all()
        form = CompanyForm(instance=company)
        return render(request, 'tasks/companies/company_edit.html', {'form': form, 'company': company, 'all_users': all_users})

    def post(self, request, pk):
        company = Company.objects.get(pk=pk)
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            company = form.save()

            # Обрабатываем приглашения и добавляем участников
            invite_emails = request.POST.getlist('invite_email[]')
            for email in invite_emails:
                user, created = User.objects.get_or_create(email=email)
                if created:
                    # Отправляем приглашение, если пользователь новый
                    self.send_invitation(company, request.user, email)

                # Добавляем пользователя в компанию
                company.members.add(user)

            return redirect('company_edit', pk=company.pk)  # Перенаправление на редактирование компании

        else:
            print(form.errors)  # Вывод ошибок формы для отладки
            all_users = User.objects.all()
            return render(request, 'tasks/companies/company_edit.html', {'form': form, 'company': company, 'all_users': all_users})

    def send_invitation(self, company, sender, email):
        subject = f'Приглашение присоединиться к компании {company.name}'
        message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
        send_mail(subject, message, sender.email, [email])


# Представление для детальной информации о компании
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'tasks/companies/company_detail.html'
    context_object_name = 'company'


def home_view(request):
    if request.user.is_authenticated:
        return redirect('task_list_all')
        # Если пользователь аутентифицирован, показываем список всех задач
        # companies = Company.objects.all()
        # return render(request, 'tasks/task_list_all.html', {'companies': companies})
    else:
        # Если не аутентифицирован, показываем приветственную страницу
        return render(request, 'account/welcome.html')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'tasks/companies/company_confirm_delete.html'  # Шаблон подтверждения удаления
    success_url = reverse_lazy('company_list')  # Перенаправление на список компаний после успешного удаления


# Представление для просмотра списка Задач
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'  # Имя контекста для доступа к задачам в шаблоне
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        # Получаем company_id из GET-запроса
        company_id = self.request.GET.get('company_id')
        if company_id:
            return Task.objects.filter(company_id=company_id)  # Фильтруем по компании
        return Task.objects.all()  # Возвращаем все задачи, если company_id не указан

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.request.GET.get('company_id')

        # Если company_id указан, получаем соответствующую компанию
        if company_id:
            context['selected_company'] = get_object_or_404(Company, id=company_id)
        else:
            context['selected_company'] = None  # Нет выбранной компании

        # Получаем все компании для отображения в фильтре
        context['companies'] = Company.objects.all()
        return context


# Представление для удаления Задачи
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'tasks/task_delete'
    success_url = reverse_lazy('tasks/task_list')  # Убедитесь, что у вас правильно настроен success_url

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


# class TaskCreateView(CreateView):
#     model = Task
#     form_class = TaskForm
#     template_name = 'tasks/task_create.html'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         company_id = self.kwargs.get('company_id')
#         company = get_object_or_404(Company, id=company_id)
#         kwargs['company'] = company  # Передаем компанию в форму
#         return kwargs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         company_id = self.kwargs.get('company_id')
#         company = get_object_or_404(Company, id=company_id)
#         context['company_users'] = company.members.all()  # Список пользователей компании
#         return context
#
#     def form_valid(self, form):
#         # Получаем компанию, которая привязана к задаче
#         company_id = self.kwargs.get('company_id')
#         company = get_object_or_404(Company, id=company_id)
#         form.instance.company = company
#         form.instance.author = self.request.user  # Привязываем автора задачи (пользователя)
#
#         # Сохраняем задачу
#         task = form.save()
#
#         # Получаем данные подзадач и сохраняем их
#         subtasks_data = self.request.POST.get('subtasks')
#         if subtasks_data:
#             subtasks = json.loads(subtasks_data)  # Десериализуем JSON
#             for subtask_data in subtasks:
#                 SubTask.objects.create(
#                     task=task,
#                     title=subtask_data['subtaskTitle'],
#                     assigned_user_id=subtask_data['executor'],  # Убедитесь, что это ID пользователя
#                     due_date=subtask_data['dueDate'],
#                     description=subtask_data.get('description', '')
#                 )
#
#         # Возвращаем стандартное поведение сохранения формы
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('task_list', kwargs={'company_id': self.kwargs['company_id']})


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        company_id = self.kwargs.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        kwargs['company'] = company  # Передаем компанию в форму
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        context['company_users'] = company.members.all()  # Список пользователей компании
        return context

    def form_valid(self, form):
        # Получаем компанию, которая привязана к задаче
        company_id = self.kwargs.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        form.instance.company = company
        form.instance.author = self.request.user  # Привязываем автора задачи (пользователя)

        # Сохраняем задачу
        task = form.save()

        # Получаем данные подзадач и сохраняем их
        subtasks_data = self.request.POST.get('subtasks')
        if subtasks_data:
            subtasks = json.loads(subtasks_data)  # Десериализуем JSON
            for subtask_data in subtasks:
                SubTask.objects.create(
                    task=task,
                    title=subtask_data['subtaskTitle'],  # Поле title модели SubTask
                    status=subtask_data.get('status', False)  # Поле status модели SubTask
                )

        # Возвращаем стандартное поведение сохранения формы
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_list', kwargs={'company_id': self.kwargs['company_id']})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # Получаем идентификатор компании из URL
        company_id = self.kwargs.get('company_id')
        data['company_id'] = company_id  # передаем company_id в шаблон
        # Загрузка подзадач через formset
        if self.request.POST:
            data['subtasks'] = SubTaskFormSet(self.request.POST, instance=self.object)
        else:
            data['subtasks'] = SubTaskFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']
        # Сохраняем задачу и подзадачи вместе
        if form.is_valid() and subtasks.is_valid():
            form.save()
            subtasks.instance = self.object
            subtasks.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        # Перенаправление на список задач компании после сохранения
        return reverse_lazy('tasks/task_list', kwargs={'company_id': self.kwargs.get('company_id')})


class TaskListAllView(ListView):
    model = Task
    template_name = 'tasks/task_list_all.html'  # Шаблон для отображения всех задач
    context_object_name = 'tasks'

    def get_queryset(self):
        # Получаем company_id из GET-запроса
        company_id = self.request.GET.get('company_id')

        # Фильтруем задачи по company_id, если он указан
        if company_id:
            return Task.objects.filter(company__id=company_id)

        return Task.objects.all()  # Возвращает все задачи, если company_id не указан

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_id'] = self.request.GET.get('company_id')  # Динамически передаем ID компании
        context['companies'] = Company.objects.all()  # Получаем список всех компаний для отображения в селекте
        return context

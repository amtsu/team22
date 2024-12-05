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
        form = CompanyForm()
        all_users = User.objects.all()
        return render(
            request,
            'tasks/companies/company_create.html',
            {
                'form': form,
                'all_users': all_users,
                'selected_members': [],
            }
        )

    def post(self, request):
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save()

            # Обработка выбранных участников и приглашенных по email
            selected_members = json.loads(request.POST.get('selected_members', '[]'))
            new_members = []

            for member in selected_members:
                if member['type'] == 'registered':
                    # Если участник выбран из зарегистрированных пользователей
                    user = User.objects.get(id=member['id'])
                    new_members.append(user)
                # elif member['type'] == 'email':
                    # Если участник приглашен по email
                    # user, created = User.objects.get_or_create(
                    #     email=member['email'],
                    #     defaults={'username': member['email'].split('@')[0]}
                    # )
                    # new_members.append(user)

                    # if created:
                    #     # Отправляем приглашение новому пользователю
                    #     self.send_invitation(company, request.user, member['email'])

            # Заполняем поле members
            company.members.set(new_members)  # Заменяем всех участников новыми

            return redirect('company_list')  # Перенаправление на список компаний
        else:
            print(form.errors)  # Для отладки
            all_users = User.objects.all()
            return render(
                request,
                'tasks/companies/company_create.html',
                {
                    'form': form,
                    'all_users': all_users,
                    'selected_members': [],
                }
            )

    # def send_invitation(self, company, sender, email):
    #     """Функция для отправки приглашения по email."""
    #     subject = f'Приглашение присоединиться к компании {company.name}'
    #     message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
    #     send_mail(subject, message, sender.email, [email])


class CompanyEditView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        all_users = User.objects.all()
        form = CompanyForm(instance=company)

        # Собираем текущих участников компании
        selected_members = [
            {"id": user.id, "username": user.username}
            for user in company.members.all()
        ]

        return render(
            request,
            'tasks/companies/company_edit.html',
            {
                'form': form,
                'company': company,
                'all_users': all_users,
                'selected_members': selected_members,
                'selected_members_json': json.dumps(selected_members),
            }
        )

    def post(self, request, pk):
        company = Company.objects.get(pk=pk)
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            company = form.save()

            # Обработка участников
            try:
                selected_members = json.loads(request.POST.get('selected_members', '[]'))
            except json.JSONDecodeError:
                selected_members = []

            members = []
            for member in selected_members:
                try:
                    user = User.objects.get(id=member['id'])
                    members.append(user)
                except User.DoesNotExist:
                    continue  # Пропускаем, если пользователь не найден

            company.members.set(members)  # Обновляем список участников

            return redirect('company_detail', pk=company.pk)

        else:
            all_users = User.objects.all()
            try:
                selected_members = json.loads(request.POST.get('selected_members', '[]'))
            except json.JSONDecodeError:
                selected_members = []

            return render(
                request,
                'tasks/companies/company_edit.html',
                {
                    'form': form,
                    'company': company,
                    'all_users': all_users,
                    'selected_members': selected_members,
                    'selected_members_json': json.dumps(selected_members),
                }
            )

    # def send_invitation(self, company, sender, email):
    #     subject = f'Приглашение присоединиться к компании {company.name}'
    #     message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
    #     send_mail(subject, message, sender.email, [email])


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


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list_all.html'  # Убедитесь, что этот путь соответствует вашему шаблону

    def get_queryset(self):
        company_id = self.request.GET.get('company_id')
        if company_id:  # Если указана компания
            return Task.objects.filter(company_id=company_id)
        return Task.objects.all()  # Возвращаем все задачи, если компания не выбрана

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.request.GET.get('company_id')

        # Если компания выбрана, добавляем её в контекст
        if company_id:
            context['selected_company'] = get_object_or_404(Company, id=company_id)
        else:
            context['selected_company'] = None  # Все компании

        # Передаем список всех компаний в шаблон
        context['companies'] = Company.objects.all()
        return context


# Представление для удаления Задачи
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'tasks/task_delete'
    # success_url = reverse_lazy('tasks/task_list')  # Убедитесь, что у вас правильно настроен success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.object.company  # Предполагается, что у задачи есть поле company
        context['company'] = company if company else None
        return context

    def get_success_url(self):
        return reverse_lazy('company_detail', kwargs={'company_id': self.kwargs['company_id']})


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

        # Создаем formset для подзадач
        if self.request.POST:
            context['subtask_formset'] = SubTaskFormSet(self.request.POST)
        else:
            context['subtask_formset'] = SubTaskFormSet()

        return context

    def form_valid(self, form):
        company_id = self.kwargs.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        form.instance.company = company
        form.instance.author = self.request.user  # Привязываем автора задачи (пользователя)

        # Сохраняем задачу
        task = form.save()

        # Получаем и сохраняем подзадачи
        subtask_formset = SubTaskFormSet(self.request.POST)
        if subtask_formset.is_valid():
            # Сохраняем все подзадачи
            subtask_formset.instance = task  # Привязываем подзадачи к только что созданной задаче
            subtask_formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        company_id = self.kwargs.get('company_id')  # Получаем ID компании из URL
        return reverse_lazy('company_detail', kwargs={'pk': company_id})  # Используем company_id для перенаправления на компанию


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.object.company
        context['company'] = company if company else None
        return context

    def get_success_url(self):
        # Возвращаем URL страницы с деталями компании
        return reverse_lazy('company_detail', kwargs={'pk': self.object.company.id})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'

    def get_object(self, queryset=None):
        # Получаем задачу по её ID
        return get_object_or_404(Task, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем ID компании из URL
        company_id = self.kwargs['company_id']
        company = get_object_or_404(Company, id=company_id)
        context['users'] = company.members.all()  # Фильтруем пользователей по компании
        context['company_id'] = company.id  # Добавляем ID компании в контекст
        return context

    def form_valid(self, form):
        # Сохраняем данные формы
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # После успешного редактирования задачи переходим на список задач компании
        company_id = self.kwargs['company_id']
        return reverse_lazy('tasks:task_list', kwargs={'company_id': company_id})


class TaskListAllView(ListView):
    model = Task
    template_name = 'tasks/task_list_all.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        company_id = self.request.GET.get('company_id')
        if company_id:  # Если выбрана компания
            return Task.objects.filter(company__id=company_id)
        return Task.objects.all()  # Если выбраны все компании

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.request.GET.get('company_id', '')

        context['company_id'] = company_id  # Для сохранения выбора компании в фильтре
        context['companies'] = Company.objects.all()  # Список всех компаний

        # Добавляем выбранную компанию в контекст
        if company_id:
            context['selected_company'] = Company.objects.filter(id=company_id).first()
        else:
            context['selected_company'] = None

        return context

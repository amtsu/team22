from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import View

from django.core.mail import send_mail
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import TaskForm, SubTaskFormSet, CompanyForm
from .models import Task, Company


# Представление для просмотра списка компаний
class CompanyListView(ListView):
    model = Company
    template_name = 'tasks/companies/company_list.html'
    context_object_name = 'companies'  # Имя переменной, доступной в шаблоне

    def get_queryset(self):
        return Company.objects.all()  # Возвращает все объекты компании


# Представление для создания компании

class CompanyCreateView(View):
    def get(self, request):
        form = CompanyForm()
        return render(request, 'tasks/companies/company_create.html', {'form': form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()

            # Получаем email для приглашения
            invite_emails = request.POST.getlist('invite_email[]')
            for email in invite_emails:
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={'username': email}
                )
                if created:
                    self.send_invitation(company, request.user, email)
                company.members.add(user)

            return redirect('company_list')

        return render(request, 'tasks/create_company.html', {'form': form})

    def send_invitation(self, company, sender, email):
        subject = f'Приглашение в компанию {company.name}'
        message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
        send_mail(subject, message, sender.email, [email])

    def post_invite(self, request):
        if request.is_ajax() and request.method == "POST":
            email = request.POST.get('email')
            user, created = User.objects.get_or_create(
                email=email,
                defaults={'username': email}
            )
            if created:
                company = Company.objects.get(id=request.POST.get('company_id'))
                company.members.add(user)

                return JsonResponse({
                    'success': True,
                    'user_id': user.id,
                    'username': user.username
                })
            else:
                return JsonResponse({'success': False, 'message': 'User already exists'}, status=400)

        return JsonResponse({'success': False}, status=400)

# class CompanyCreateView(CreateView):
#     model = Company
#     form_class = CompanyForm
#     template_name = 'tasks/companies/company_create.html'
#     success_url = reverse_lazy('company_list')  # Переход на список компаний после создания
#
#     def form_valid(self, form):
#         # Устанавливаем текущего пользователя как владельца компании
#         form.instance.owner = self.request.user
#         # Сохраняем компанию
#         response = super().form_valid(form)
#
#         # Получаем список email для приглашений
#         invite_emails = self.request.POST.getlist('invite_email')
#
#         for invite_email in invite_emails:
#             if invite_email:  # Проверка, что поле не пустое
#                 # Проверка, существует ли email в базе данных
#                 user = User.objects.filter(email=invite_email).first()
#                 if not user:
#                     # Если пользователь не найден, отправляем приглашение
#                     send_mail(
#                         'Приглашение в программу',
#                         f'Вы приглашены в компанию {form.instance.name} в приложении SuperKanban.',
#                         'noreply@superkanban.com',
#                         [invite_email]
#                     )
#                     # Логика для добавления временного пользователя
#                     # Пример: создаем пользователя и добавляем его в компанию
#                     new_user = User.objects.create_user(email=invite_email, username=invite_email.split('@')[0])
#                     form.instance.members.add(new_user)
#
#         return response


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


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'tasks/companies/company_edit.html'

    def form_valid(self, form):
        # Сохраняем изменения
        company = form.save()

        # Обрабатываем приглашения и добавляем участников
        invite_emails = self.request.POST.getlist('invite_email[]')
        for email in invite_emails:
            user, created = User.objects.get_or_create(email=email)
            if created:
                # Отправляем приглашение, если пользователь новый
                self.send_invitation(company, self.request.user, email)

            # Добавляем пользователя в компанию
            company.members.add(user)

        return redirect('company_edit', pk=company.pk)  # Перенаправление на редактирование компании

    def send_invitation(self, company, sender, email):
        subject = f'Приглашение присоединиться к компании {company.name}'
        message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
        send_mail(subject, message, sender.email, [email])


# def remove_member(request, member_id, company_id):
#     company = get_object_or_404(Company, id=company_id)
#     member = get_object_or_404(User, id=member_id)
#
#     if member in company.members.all():
#         company.members.remove(member)  # Удаляем участника из компании
#
#     return redirect('company_edit', company_id=company.id)  # Перенаправляем обратно на страницу редактирования компании
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


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    context_object_name = 'task_create'

    # Заменяем success_url для перенаправления после создания задачи
    def get_success_url(self):
        return reverse_lazy('tasks/task_list', kwargs={'company_id': self.kwargs['company_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передаем company_id в контекст
        context['company_id'] = self.kwargs.get('company_id')

        # Проверяем, если данные переданы через POST, инициализируем подзадачи с данными
        if self.request.POST:
            context['subtasks'] = SubTaskFormSet(self.request.POST)
        else:
            context['subtasks'] = SubTaskFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        subtasks = context['subtasks']
        form.instance.author = self.request.user

        # Связываем задачу с компанией
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

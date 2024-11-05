from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Company, Task
from .forms import CompanyForm, TaskForm


class CompanyCreationTest(TestCase):

    def setUp(self):
        # Создаем пользователя для использования в тестах
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    def test_create_company_success(self):
        ''' Тест, который проверяет успешное создание компании'''
        # Данные для создания компании
        form_data = {
            'name': 'Test Company',
            'members': [self.user.id]  # Добавляем пользователя в качестве члена
        }

        # Создаем форму с данными
        form = CompanyForm(data=form_data)

        # Проверяем, что форма валидна:
        # Все обязательные поля заполнены,
        # Поля имеют правильные типы данных
        # Все правила валидации, которые мы задали в форме или модели, были соблюдены.
        self.assertTrue(form.is_valid())

        # Сохраняем компанию
        company = form.save(commit=True)

        # Проверяем, что компания создана и ее имя корректно
        self.assertEqual(company.name, 'Test Company')
        self.assertIn(self.user, company.members.all())  # Проверяем, что пользователь - член компании


class TaskCreationTest(TestCase):
    ''' Тест, который проверяет создание задачи'''
    def setUp(self):
        # Создаем пользователя для теста
        self.user = User.objects.create_user(username='testuser', password='password', email='user@example.com')
        # Создаем компанию для теста
        self.company = Company.objects.create(name='Test Company')

    def test_task_creation(self):
        # Данные для создания задачи
        form_data = {
            'title': 'Test Task',
            'description': 'Тест для создания задачи',
            'execution_status': 'AC',
            'due_date': timezone.now().date() + timezone.timedelta(days=1),  # Завтрашняя дата
            'assigned_user': self.user.id,  # Назначаем пользователю
            'company': self.company.id,  # Назначаем компании
        }

        # Создаем форму с пользователем
        form = TaskForm(data=form_data, user=self.user)  # Передаем пользователя в форму
        self.assertTrue(form.is_valid(), msg=form.errors)  # Проверяем, что форма валидна

        # Сохраняем задачу
        task = form.save()

        # Проверяем, что задача была создана
        self.assertEqual(task.title, 'Test Task')  # Проверяем, что задача создана
        self.assertEqual(task.author, self.user)  # Проверяем, что автор задачи соответствует пользователю
        self.assertEqual(task.company, self.company)  # Проверяем, что задача относится к правильной компании


class TaskEditingTest(TestCase):
    ''' Тест, который проверяет редактирование задачи'''
    def setUp(self):
        # Создаем пользователя для теста
        self.user = User.objects.create_user(username='testuser', password='password', email='user@example.com')
        # Создаем компанию для теста
        self.company = Company.objects.create(name='Test Company')
        # Создаем задачу для редактирования
        self.task = Task.objects.create(
            title='Оригинал Task',
            description='Оригинал задачи.',
            execution_status='AC',
            due_date=timezone.now().date() + timezone.timedelta(days=1),  # Завтрашняя дата
            author=self.user,
            assigned_user=self.user,
            company=self.company
        )

    def test_task_editing(self):
        # Данные для редактирования задачи
        form_data = {
            'title': 'Updated Task',
            'description': 'Измененная задача.',
            'execution_status': 'CP',  # Обновляем статус на завершенную
            'due_date': timezone.now().date() + timezone.timedelta(days=2),  # Изменяем дату завершения
            'assigned_user': self.user.id,  # Назначаем пользователю
            'company': self.company.id,  # Назначаем компании
        }

        # Создаем форму с данными редактирования
        form = TaskForm(instance=self.task, data=form_data, user=self.user)  # Передаем текущую задачу

        # Проверяем, что форма валидна
        self.assertTrue(form.is_valid(), msg=form.errors)  # Проверяем, что форма валидна

        # Сохраняем задачу
        updated_task = form.save()

        # Проверяем, что задача была обновлена
        self.assertEqual(updated_task.title, 'Updated Task')  # Проверяем, что заголовок задачи обновлен
        self.assertEqual(updated_task.description, 'Измененная задача.')  # Проверяем, что описание обновлено
        self.assertEqual(updated_task.execution_status, 'CP')  # Проверяем, что статус задачи обновлен на завершенный
        self.assertEqual(updated_task.due_date, timezone.now().date() + timezone.timedelta(days=2))  # Проверяем новую дату завершения
        self.assertEqual(updated_task.assigned_user, self.user)  # Проверяем, что задача по-прежнему назначена пользователю
        self.assertEqual(updated_task.company, self.company)  # Проверяем, что задача по-прежнему относится к правильной компании


class PagesTest(TestCase):

    def test_task_list_all(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_companies(self):
        response = self.client.get('/companies/')
        self.assertEqual(response.status_code, 200)
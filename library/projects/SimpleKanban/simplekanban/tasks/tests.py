# simplekanban/tasks/tests.py

from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import Task, Company
from .forms import TaskForm
from datetime import timedelta
from django.test import TestCase

class TaskStatusChangeTests(TestCase):

    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.user = User.objects.create(username='testuser', password='password')
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            execution_status='active',
            due_date=now() - timedelta(days=1),  # Вчерашняя дата
            author=self.user,
            company=self.company
        )

    def test_task_status_change_to_overdue(self):
        # Проверка, что статус задачи меняется на 'overdue' по истечению срока выполнения
        self.task.refresh_from_db()  # Обновляем задачу из базы данных
        self.assertTrue(self.task.execution_status == 'overdue', "Статус задачи не изменился на 'overdue'")

    def test_task_creation(self):
        # Проверка создания задачи и её перемещения в 'overdue'
        task_data = {
            'title': "New Task",
            'description': "New Task Description",
            'execution_status': 'active',
            'due_date': now() - timedelta(days=1),
            'author': self.user.id,
            'company': self.company.id
        }
        form = TaskForm(task_data)
        self.assertTrue(form.is_valid(), "Форма задачи невалидна")
        task = form.save()
        self.assertTrue(task.execution_status == 'overdue', "Статус задачи не изменился на 'overdue'")
        self.assertTrue(task.due_date < now(), "Срок выполнения задачи не истек")

    def test_task_update_status(self):
        # Проверка обновления задачи и её перемещения в 'overdue'
        task = self.task
        task.due_date = now() - timedelta(days=1)
        task.save()
        task.refresh_from_db()  # Обновляем задачу из базы данных
        self.assertTrue(task.execution_status == 'overdue', "Статус задачи не изменился на 'overdue'")


from django.test import TestCase
from django.utils import timezone
# from django.contrib.auth.models import User
# from .models import Company, Task
# from .forms import CompanyForm, TaskForm
#

# class BaseTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         """ Фикстуры, общие для всех тестов """
#         # Создаем пользователя для использования в тестах
#         cls.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
#
#         # Создаем компанию для использования в тестах  и назначаем владельца
#         cls.company = Company.objects.create(name='Test Company', owner=cls.user)


# class CompanyModelTest(BaseTestCase):
#     def test_company_creation(self):
#         # Используем общую фикстуру company, которая уже создана
#         self.assertEqual(self.company.name, 'Test Company')
#         self.assertEqual(self.company.owner, self.user)
#
#     def test_members_relation(self):
#         # Проверяем добавление участников в компанию
#         self.company.members.add(self.user)
#         self.assertIn(self.user, self.company.members.all())


# class CompanyCreationTest(BaseTestCase):
#     def test_create_company_success(self):
#         ''' Тест, который проверяет успешное создание компании'''
#         # Данные для создания компании
#         form_data = {
#             'name': 'Test Company',
#             'members': [self.user.id]  # Добавляем пользователя в качестве члена
#         }
#
#         # Создаем форму с данными
#         form = CompanyForm(data=form_data)

        # Проверяем, что форма валидна:
        # Все обязательные поля заполнены,
        # Поля имеют правильные типы данных
        # Все правила валидации, которые мы задали в форме или модели, были соблюдены.
        # self.assertTrue(form.is_valid())
        #
        # # Сохраняем компанию
        # company = form.save(commit=True)
        #
        # # Проверяем, что компания создана и ее имя корректно
        # self.assertEqual(company.name, 'Test Company')
        # self.assertIn(self.user, company.members.all())  # Проверяем, что пользователь - член компании

#
# # class TaskCreationTest(BaseTestCase):
# #     ''' Тест, который проверяет создание задачи'''
# #
# #     def test_task_creation(self):
# #         # Данные для создания задачи
# #         form_data = {
# #             'title': 'Test Task',
# #             'description': 'Тест для создания задачи',
# #             'execution_status': 'AC',
# #             'due_date': timezone.now().date() + timezone.timedelta(days=1),  # Завтрашняя дата
# #             'assigned_user': self.user.id,  # Назначаем пользователю
# #             'company': self.company.id,  # Назначаем компании
# #         }
# #
# #         # Создаем форму с пользователем
# #         form = TaskForm(data=form_data, user=self.user)  # Передаем пользователя в форму
# #         self.assertTrue(form.is_valid(), msg=form.errors)  # Проверяем, что форма валидна
# #
# #         # Сохраняем задачу
# #         task = form.save()
# #
# #         # Проверяем, что задача была создана
# #         self.assertEqual(task.title, 'Test Task')  # Проверяем, что задача создана
# #         self.assertEqual(task.author, self.user)  # Проверяем, что автор задачи соответствует пользователю
# #         self.assertEqual(task.company, self.company)  # Проверяем, что задача относится к правильной компании
# #
# #
# # class TaskEditingTest(BaseTestCase):
# #     ''' Тест, который проверяет редактирование задачи'''
# #     def setUp(self):
# #         # Создаем задачу для редактирования
# #         self.task = Task.objects.create(
# #             title='Оригинал Task',
# #             description='Оригинал задачи.',
# #             execution_status='AC',
# #             due_date=timezone.now().date() + timezone.timedelta(days=1),  # Завтрашняя дата
# #             author=self.user,
# #             assigned_user=self.user,
# #             company=self.company
# #         )
# #
# #     def test_task_editing(self):
# #         # Данные для редактирования задачи
# #         form_data = {
# #             'title': 'Updated Task',
# #             'description': 'Измененная задача.',
# #             'execution_status': 'CP',  # Обновляем статус на завершенную
# #             'due_date': timezone.now().date() + timezone.timedelta(days=2),  # Изменяем дату завершения
# #             'assigned_user': self.user.id,  # Назначаем пользователю
# #             'company': self.company.id,  # Назначаем компании
# #         }
# #
# #         # Создаем форму с данными редактирования
# #         form = TaskForm(instance=self.task, data=form_data, user=self.user)  # Передаем текущую задачу
# #
# #         # Проверяем, что форма валидна
# #         self.assertTrue(form.is_valid(), msg=form.errors)  # Проверяем, что форма валидна
# #
# #         # Сохраняем задачу
# #         updated_task = form.save()
# #
# #         # Проверяем, что задача была обновлена
# #         self.assertEqual(updated_task.title, 'Updated Task')  # Проверяем, что заголовок задачи обновлен
# #         self.assertEqual(updated_task.description, 'Измененная задача.')  # Проверяем, что описание обновлено
# #         self.assertEqual(updated_task.execution_status, 'CP')  # Проверяем, что статус задачи обновлен на завершенный
# #         self.assertEqual(updated_task.due_date, timezone.now().date() + timezone.timedelta(days=2))  # Проверяем новую дату завершения
# #         self.assertEqual(updated_task.assigned_user, self.user)  # Проверяем, что задача по-прежнему назначена пользователю
# #         self.assertEqual(updated_task.company, self.company)  # Проверяем, что задача по-прежнему относится к правильной компании
# #
#
# class PagesTest(BaseTestCase):
#
#     def test_task_list_all(self):
#         response = self.client.get('/tasks/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_companies(self):
#         response = self.client.get('/companies/')
#         self.assertEqual(response.status_code, 200)
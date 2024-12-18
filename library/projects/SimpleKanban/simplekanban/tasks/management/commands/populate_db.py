from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from tasks.models import Task, Company
from faker import Faker
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Создание группы
        group_name = fake.word()
        group, created = Group.objects.get_or_create(name=group_name)

        # Создание пользователей и добавление их в группу
        for _ in range(10):  # Создаём 10 пользователей
            username = fake.user_name()
            password = fake.password()
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.groups.add(gro3p)
                user.save()

        # Создание компаний
        for _ in range(3):  # Создаём 3 компании
            company_name = fake.company()
            Company.objects.get_or_create(name=company_name)

        # Создание задач для каждой компании
        users = list(User.objects.all())
        companies = Company.objects.all()
        for company in companies:
            for _ in range(6):  # Создаём 6 задач для каждой компании
                title = fake.sentence(nb_words=6)
                description = fake.text()
                assigned_user = fake.random_element(users)
                due_date = timezone.now() + timedelta(days=7)
                Task.objects.create(
                    title=title,
                    description=description,
                    author=assigned_user,
                    assigned_user=assigned_user,
                    company=company,
                    due_date=due_date
                )

        self.stdout.write(self.style.SUCCESS('Database populated with random data successfully'))


# python manage.py populate_db  - команда для запуска кода данного файла

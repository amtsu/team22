from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from tasks.models import Task, SubTask, Company
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Создание группы
        group_name = fake.word()
        group, created = Group.objects.get_or_create(name=group_name)

        # Создание пользователей и добавление их в группу
        for _ in range(20):  # Создаём 20 пользователей
            username = fake.user_name()
            password = fake.password()
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.groups.add(group)
                user.save()

        # Создание компаний
        for _ in range(7):  # Создаём 7 компаний
            company_name = fake.company()
            Company.objects.get_or_create(name=company_name)

        # Создание задач
        users = User.objects.all()
        companies = Company.objects.all()
        for _ in range(20):  # Создаём 20 задач
            title = fake.sentence(nb_words=6)
            description = fake.text()
            assigned_to = fake.random_element(users)
            company = fake.random_element(companies)
            Task.objects.get_or_create(
                title=title,
                description=description,
                assigned_to=assigned_to,
                company=company
            )

        self.stdout.write(self.style.SUCCESS('Database populated with random data successfully'))

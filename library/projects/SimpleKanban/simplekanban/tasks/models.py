from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(
        max_length=255
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='owned_companies'
    )
    members = models.ManyToManyField(
        User,
        related_name='companies'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    EXECUTION_STATUS_CHOICES = [
        ("AC", "активная"),
        ("EX", "просроченная"),
        ("CP", "завершенная"),
        ("CN", "отмененная"),
    ]
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        default=1,
        related_name='tasks'
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Задача"
    )
    description = models.TextField(
        "Описание",
        blank=True,
        null=True
    )
    execution_status = models.CharField(
        'Статус выполнения',
        choices=EXECUTION_STATUS_CHOICES,
        default='AC',
        max_length=50
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        verbose_name="Автор")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")
    due_date = models.DateField(
        verbose_name="Дата завершения")
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        verbose_name='Назначенный пользователь'
    )
    attachment = models.FileField(
        upload_to='task_attachments/',  # Папка для загрузки файлов
        null=True, blank=True,  # Можно оставлять поле пустым
        verbose_name='Файл'
    )

    def __str__(self):
        return self.title

    def clean(self):
        # Проверка, что дата завершения не может быть в прошлом
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError('Дата завершения не может быть в прошлом.')

        # Проверка, что дата завершения не может быть ранее даты создания
        if self.created_at and (self.due_date and self.due_date < self.created_at.date()):
            raise ValidationError('Дата завершения не может быть ранее даты создания.')

    def save(self, *args, **kwargs):
        # Обновление статуса на основе даты завершения
        if self.due_date and self.due_date < timezone.now():
            self.execution_status = 'EX'  # Обновляем статус, если задача просрочена
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class SubTask(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="subtasks",
        verbose_name="Основная задача"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Подзадача"
    )
    status = models.BooleanField(
        default=False,
        verbose_name="Статус выполнения"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подзадача"
        verbose_name_plural = "Подзадачи"

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class WorkGroup(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название группы'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workgroup_owner',
        verbose_name='Владелец'
    )
    admins = models.ManyToManyField(
        User,
        related_name='workgroup_admins',
        verbose_name='Администраторы',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рабочая группа'
        verbose_name_plural = 'Рабочие группы'


class Task(models.Model):
    EXECUTION_STATUS_CHOICES = [
        ("AC", "активная"),        # Active
        ("EX", "просроченная"),       # Expired
        ("CP", "завершенная"),     # Completed
        ("CN", "отмененная"),      # Canceled
    ]

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
    work_group = models.ForeignKey(
        'WorkGroup',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Рабочая группа')

    def __str__(self):
        return self.title

    def clean(self):
        # Проверка, что дата завершения не может быть в прошлом
        if self.due_date < timezone.now().date():
            raise ValidationError('Дата завершения не может быть в прошлом.')

        # Проверка, что дата завершения не может быть ранее даты создания
        if self.created_at and self.due_date < self.created_at.date():
            raise ValidationError('Дата завершения не может быть ранее даты создания.')

    def save(self, *args, **kwargs):
        # Обновление статуса на основе даты завершения
        if self.due_date < timezone.now().date():
            self.execution_status = 'EX'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

# class Task(models.Model):
#     EXECUTION_STATUS_CHOICES = [
#         ("AC", "активная"),        # Active
#         ("EX", "просроченная"),       # Expired
#         ("CP", "завершенная"),     # Completed
#         ("CN", "отмененная"),      # Canceled
#     ]
#     title = models.CharField(
#         max_length=100,
#         verbose_name="Задача"
#     )
#     description = models.TextField(
#         "Описание",
#         blank=True,
#         null=True
#     )
#     execution_status = models.CharField(
#         'Статус выполнения',
#         choices=EXECUTION_STATUS_CHOICES,
#         default='AC',
#         max_length=50
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='created_tasks',
#         verbose_name="Автор"
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Дата создания"
#     )
#     due_date = models.DateField(
#         verbose_name="Дата завершения"
#     )
#     assigned_user = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='assigned_tasks',  # Уникальное имя для назначенного пользователя
#         verbose_name='Назначенный пользователь'
#     )
#     work_group = models.ForeignKey(
#         WorkGroup,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         verbose_name='Рабочая группа'
#     )
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Задача"
#         verbose_name_plural = "Задачи"


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

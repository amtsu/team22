from django.contrib.auth.models import User

from django.db import models


class Task(models.Model):
    EXECUTION_STATUS_CHOICES = [
        ("AC", "Active"),        # активная
        ("EX", "Expired"),       # просроченная
        ("CP", "Completed"),     # завершенная
        ("CN", "Canceled"),      # отмененная
    ]
    title = models.CharField(max_length=100, verbose_name='Задача')
    description = models.TextField('Описание', blank=True, null=True)
    execution_status = models.CharField(
        'Статус выполнения',
        choices=EXECUTION_STATUS_CHOICES,
        default='AC',
        max_length=50
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    due_date = models.DateField(verbose_name='Дата завершения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

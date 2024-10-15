from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

from .models import Task, SubTask, WorkGroup


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'execution_status', 'due_date', 'work_group', 'assigned_user']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'execution_status': forms.Select(choices=Task.EXECUTION_STATUS_CHOICES),
        }

    #чтобы поле автор был автоматически заполнено текущим пользователем:
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем текущего пользователя
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].initial = user  # Устанавливаем текущего пользователя в качестве автора
            self.fields['author'].widget.attrs['readonly'] = True  # Делаем поле автор только для чтения


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'task']


class WorkGroupForm(forms.ModelForm):
    admins = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Администраторы'
    )

    class Meta:
        model = WorkGroup
        fields = ['title', 'owner', 'admins']


# Создаем formset для подзадач, связанный с моделью задачи
SubTaskFormSet = inlineformset_factory(
    Task,  # Модель задачи (родительская модель)
    SubTask,  # Модель подзадачи (вложенная модель)
    form=SubTaskForm,
    extra=1,  # Количество пустых форм для добавления новых подзадач
    can_delete=True  # Возможность удаления подзадач
)

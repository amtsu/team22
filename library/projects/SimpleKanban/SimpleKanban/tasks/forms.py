from django import forms

from tasks.models import Task

# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'execution_status', 'author', 'execution_status', 'due_date']
        widgets = {
            #<input type="date" name="due_date"> - добавить в html
            'due_date': forms.DateInput(attrs={'type': 'date'}),                      # Используем HTML5 date input
            # 'execution_status': forms.Select(choices=Task.EXECUTION_STATUS_CHOICES),  # Делаем выбор статуса-выпад список в html
        }

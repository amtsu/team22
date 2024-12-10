from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Task, SubTask, Company


class CompanyForm(forms.ModelForm):
    invitees = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите email для приглашения, разделяя их запятой'}
        )
    )

    class Meta:
        model = Company
        fields = ['name', 'members']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    # Делает поле 'members' необязательным
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].required = False


class InviteForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))

    def send_invitation(self, company, sender):
        email = self.cleaned_data['email']
        subject = f'Приглашение присоединиться к компании {company.name}'
        message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
        send_mail(subject, message, sender.email, [email])


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'execution_status', 'due_date', 'assigned_user', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание задачи'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'execution_status': forms.Select(attrs={'class': 'form-control'}),
            'assigned_user': forms.Select(attrs={'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)  # Получаем компанию из вьюхи
        super().__init__(*args, **kwargs)  # Сначала вызываем super()

        # Инициализация поля due_date
        if self.instance and self.instance.due_date:
            self.fields['due_date'].initial = self.instance.due_date.strftime('%Y-%m-%d')



        # # Фильтруем поле assigned_user только для пользователей компании
        # if company:
        #     self.fields['assigned_user'].queryset = company.members.all()  # users, которые принадлежат компании
        # else:
        #     self.fields['assigned_user'].queryset = User.objects.none()  # Нет пользователей, если компании нет
        if company:
            members_queryset = company.members.all()
            # print("Company members in TaskForm:", members_queryset)  # Отладка
            self.fields['assigned_user'].queryset = members_queryset
        else:
            # print("No company provided to TaskForm")
            self.fields['assigned_user'].queryset = User.objects.none()

        # # Отладка
        # print("Assigned user queryset:", self.fields['assigned_user'].queryset)
        # print("Assigned user initial:", self.initial.get('assigned_user'))

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'task']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название подзадачи*'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
        }


# Создаем formset для подзадач, связанный с моделью задачи
SubTaskFormSet = inlineformset_factory(
    Task,
    SubTask,
    form=SubTaskForm,
    extra=1,
    can_delete=True
)

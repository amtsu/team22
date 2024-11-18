from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Task, SubTask, Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'members']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_owner(self):
        owner = self.cleaned_data.get('owner')
        if not owner:
            raise forms.ValidationError('Компания должна иметь владельца.')
        return owner


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
        fields = ['title', 'description', 'execution_status', 'due_date', 'assigned_user', 'company']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание задачи*'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'execution_status': forms.Select(attrs={'class': 'form-control'}),
            'assigned_user': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        task = super().save(commit=False)
        if self.user:
            task.author = self.user
        if commit:
            task.save()
        return task


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


# from django import forms
# from django.forms.models import inlineformset_factory
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
#
# from .models import Task, SubTask, Company
#
#
# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ['name', 'members']
#
#     def clean_owner(self):
#         owner = self.cleaned_data.get('owner')
#         if not owner:
#             raise forms.ValidationError('Компания должна иметь владельца.')
#         return owner
#
#
# class InviteForm(forms.Form):
#     email = forms.EmailField()
#
#     def send_invitation(self, company, sender):
#         # Логика отправки email приглашения
#         email = self.cleaned_data['email']
#         subject = f'Приглашение присоединиться к компании {company.name}'
#         message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
#
#         # Логика отправки email
#         send_mail(subject, message, sender.email, [email])
#
#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'execution_status', 'due_date', 'assigned_user', 'company']
#         widgets = {
#             'due_date': forms.DateInput(attrs={'type': 'date'}),
#             'execution_status': forms.Select(choices=Task.EXECUTION_STATUS_CHOICES),
#         }
#
#     def __init__(self, *args, **kwargs):
#         # Извлекаем пользователя из аргументов, если он передан
#         self.user = kwargs.pop('user', None) # Извлекаем пользователя, если он передан
#         super().__init__(*args, **kwargs)
#         # if self.user:
#         #     self.fields['author'].initial = self.user  # Устанавливаем текущего пользователя как автора
#         #     self.fields['author'].widget.attrs['readonly'] = True  # Делаем поле автор только для чтения
#
#     def save(self, commit=True):
#         task = super().save(commit=False)  # Не сохраняем еще
#         if self.user:  # Устанавливаем текущего пользователя как автора
#             task.author = self.user # Устанавливаем автора
#         if commit:  # Если нужно сохранить
#             task.save()
#         return task
#
#
# class SubTaskForm(forms.ModelForm):
#     class Meta:
#         model = SubTask
#         fields = ['title', 'task']
#
#
# # Создаем formset для подзадач, связанный с моделью задачи
# SubTaskFormSet = inlineformset_factory(
#     Task,  # Модель задачи (родительская модель)
#     SubTask,  # Модель подзадачи (вложенная модель)
#     form=SubTaskForm,
#     extra=1,  # Количество пустых форм для добавления новых подзадач
#     can_delete=True  # Возможность удаления подзадач
# )
#
# #
# # class WorkGroupForm(forms.ModelForm):
# #     admins = forms.ModelMultipleChoiceField(
# #         queryset=User.objects.all(),
# #         widget=forms.CheckboxSelectMultiple,
# #         required=False,
# #         label='Администраторы'
# #     )
# #
# #     class Meta:
# #         model = WorkGroup
# #         fields = ['title', 'owner', 'admins']
#
# from django import forms
# from django.forms.models import inlineformset_factory
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
#
# from .models import Task, SubTask, Company
#
#
# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ['name', 'members']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
#             'members': forms.SelectMultiple(attrs={'class': 'form-control'}),
#         }
#
#     def clean_owner(self):
#         owner = self.cleaned_data.get('owner')
#         if not owner:
#             raise forms.ValidationError('Компания должна иметь владельца.')
#         return owner
#
#
# class InviteForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
#
#     def send_invitation(self, company, sender):
#         email = self.cleaned_data['email']
#         subject = f'Приглашение присоединиться к компании {company.name}'
#         message = f'Вы были приглашены {sender.email} присоединиться к компании {company.name}.'
#         send_mail(subject, message, sender.email, [email])
#
#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'execution_status', 'due_date', 'assigned_user', 'company']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи*'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание задачи*'}),
#             'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'execution_status': forms.Select(attrs={'class': 'form-control'}),
#             'assigned_user': forms.Select(attrs={'class': 'form-control'}),
#             'company': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         task = super().save(commit=False)
#         if self.user:
#             task.author = self.user
#         if commit:
#             task.save()
#         return task
#
#
# class SubTaskForm(forms.ModelForm):
#     class Meta:
#         model = SubTask
#         fields = ['title', 'task']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название подзадачи*'}),
#             'task': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#
# # Создаем formset для подзадач, связанный с моделью задачи
# SubTaskFormSet = inlineformset_factory(
#     Task,
#     SubTask,
#     form=SubTaskForm,
#     extra=1,
#     can_delete=True
# )

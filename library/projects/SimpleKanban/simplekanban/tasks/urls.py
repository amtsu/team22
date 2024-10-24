from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home_view, name='home'),

    # Задачи
    path('tasks/', views.TaskListAllView.as_view(), name='task_list_all'),  # Новая строка
    path('companies/<int:company_id>/tasks/', views.TaskListView.as_view(), name='task_list'),  # Задачи для конкретной компании
    path('companies/<int:company_id>/task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),  # Детали задачи
    path('companies/<int:company_id>/task/create/', views.TaskCreateView.as_view(), name='task_create'),  # Создание задачи
    path('companies/<int:company_id>/task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),  # Редактирование задачи
    path('companies/<int:company_id>/task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),  # Удаление задачи

    # Общие задачи (если нужно, иначе можно убрать)
    path('tasks_list/', views.TaskListView.as_view(), name='task_list'),  # Задачи без фильтрации по компании

    # Компании
    path('companies/', views.CompanyListView.as_view(), name='company_list'),  # Список компаний
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),  # Создание компании
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),  # Детали компании
]

# Подзадачи - эти маршруты больше не нужны, так как подзадачи обрабатываются через formset
# path('task/<int:task_id>/subtasks/create/', views.SubTaskCreateView.as_view(), name='subtask_create'),
# path('task/<int:task_id>/subtasks/<int:pk>/edit/', views.SubTaskUpdateView.as_view(), name='subtask_edit'),
# path('task/<int:task_id>/subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask_delete'),
#
# # Рабочие группы
# path('workgroups/', views.WorkGroupListView.as_view(), name='workgroup_list'),
# path('workgroup/create/', views.WorkGroupCreateView.as_view(), name='workgroup_create'),
# path('workgroup/<int:pk>/edit/', views.WorkGroupUpdateView.as_view(), name='workgroup_edit'),
# path('workgroup/<int:pk>/delete/', views.WorkGroupDeleteView.as_view(), name='workgroup_delete'),

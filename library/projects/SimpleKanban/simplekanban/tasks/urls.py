from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home_view, name='home'),

    # Задачи
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),

    # Подзадачи - эти маршруты больше не нужны, так как подзадачи обрабатываются через formset
    # path('task/<int:task_id>/subtasks/create/', views.SubTaskCreateView.as_view(), name='subtask_create'),
    # path('task/<int:task_id>/subtasks/<int:pk>/edit/', views.SubTaskUpdateView.as_view(), name='subtask_edit'),
    # path('task/<int:task_id>/subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask_delete'),

    # Рабочие группы
    path('workgroups/', views.WorkGroupListView.as_view(), name='workgroup_list'),
    path('workgroup/create/', views.WorkGroupCreateView.as_view(), name='workgroup_create'),
    path('workgroup/<int:pk>/edit/', views.WorkGroupUpdateView.as_view(), name='workgroup_edit'),
    path('workgroup/<int:pk>/delete/', views.WorkGroupDeleteView.as_view(), name='workgroup_delete'),
]

from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.home_view, name='home'),

    # Задачи
    path('tasks/', views.TaskListAllView.as_view(), name='task_list_all'),  # Все задачи
    path('companies/<int:company_id>/tasks/', views.TaskListView.as_view(), name='task_list'),  # Задачи для конкретной компании
    path('companies/<int:company_id>/task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),  # Детали задачи
    path('companies/<int:company_id>/task/create/', views.TaskCreateView.as_view(), name='task_create'),  # Создание задачи
    path('companies/<int:company_id>/task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),  # Редактирование задачи
    path('companies/<int:company_id>/task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),  # Удаление задачи

    # Компании
    path('companies/', views.CompanyListView.as_view(), name='company_list'),  # Список компаний
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),  # Создание компании
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),  # Детали компании
]

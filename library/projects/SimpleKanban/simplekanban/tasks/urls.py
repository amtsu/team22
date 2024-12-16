from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('tasks/<int:subtask_id>/toggle_status/', views.toggle_subtask_status, name='toggle_subtask_status'),

    #Компании
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    # path('companies/post_invite/', views.InviteUserView.as_view(), name='post_invite'),  # Новый маршрут для AJAX
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<int:pk>/edit/', views.CompanyEditView.as_view(), name='company_edit'),
    path('companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

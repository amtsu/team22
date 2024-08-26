from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'), #edit лучше?
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]

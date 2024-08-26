from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'execution_status', 'author', 'created_at', 'due_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('execution_status', 'created_at')
    ordering = ('created_at', 'due_date', 'execution_status', 'author')


#admin.site.register(Task, TaskAdmin) - вместо этого декоратор @admin.register(Task)

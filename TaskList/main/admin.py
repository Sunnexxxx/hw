from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'create_at', 'deadline', 'status', 'completed_at', 'slug')
    list_display_links = ('title', 'priority', 'create_at', 'deadline')


admin.site.register(Task, TaskAdmin)
admin.site.register(ActionType)
admin.site.register(Action)

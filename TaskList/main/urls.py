from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('history/', views.task_history, name='task_history'),
    path('add/', views.add_task, name='add_task'),
    path('info/<slug:task_slug>/', views.task_info, name='task_info'),
    path('delete/<slug:task_slug>/', views.task_delete, name='task_delete'),
    path('complete/<slug:task_slug>/', views.task_complete, name='task_complete'),
    path('update/<slug:task_slug>/', views.task_update, name='task_update'),
    path('return/<slug:task_slug>/', views.task_return, name='task_return'),
    path('actions/', views.actions_table, name='actions_table'),
    path('settings/', views.settings_page, name='settings_page'),
]

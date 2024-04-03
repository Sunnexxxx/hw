from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *
from .forms import *

theme = 0
sort_by = 'title'


def task_list(request):
    tasks = Task.objects.filter(status='In progress').order_by(sort_by)
    context = {
        'title': 'Main',
        'theme': theme,
        'tasks': tasks,
    }
    return render(request, 'main/index_main.html', context)


def task_history(request):
    tasks = Task.objects.filter(status='Completed')
    context = {
        'title': 'History',
        'theme': theme,
        'tasks': tasks,
    }
    return render(request, 'main/index_history.html', context)


def add_task(request):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            action = Action.objects.create(action=ActionType.objects.get(name='Create'),
                                           date=datetime.now())
            action.save()
            return redirect('task_list')
    context = {
        'title': 'Create',
        'theme': theme,
        'form': form,
    }
    return render(request, 'main/index_add.html', context)


def task_update(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    form = AddTaskForm(initial={'title': task.title,
                                'description': task.description,
                                'priority': task.priority,
                                'deadline': task.deadline,
                                'status': task.status,
                                'image': task.image})
    if request.method == 'POST':
        form = AddTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            action = Action.objects.create(action=ActionType.objects.get(name='Edit'),
                                           date=datetime.now())
            action.save()
            return redirect('task_list')
    context = {
        'title': 'Update',
        'theme': theme,
        'form': form,
    }
    return render(request, 'main/index_update.html', context)


def task_info(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    action = Action.objects.create(action=ActionType.objects.get(name='View'),
                                   date=datetime.now())
    action.save()
    context = {
        'title': 'Info',
        'theme': theme,
        'task': task,
    }
    return render(request, 'main/index_info.html', context)


def task_delete(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    action = Action.objects.create(action=ActionType.objects.get(name='Delete'),
                                   date=datetime.now())
    action.save()
    task.delete()
    return redirect('task_list')


def task_complete(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    task.status = 'Completed'
    task.completed_at = datetime.now()
    task.save()
    action = Action.objects.create(action=ActionType.objects.get(name='Complete'),
                                   date=datetime.now())
    action.save()
    return redirect('task_list')


def task_return(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    task.status = 'In progress'
    task.completed_at = None
    task.save()
    action = Action.objects.create(action=ActionType.objects.get(name='Return'),
                                   date=datetime.now())
    action.save()
    return redirect('task_list')


def actions_table(request):
    actions = Action.objects.all()
    context = {
        'title': 'Actions',
        'theme': theme,
        'actions': actions,
    }
    return render(request, 'main/index_table.html', context)


def settings_page(request):
    global theme, sort_by
    form = SettingsForm()
    if request.method == 'POST':
        if request.POST['theme'] == 'Dark':
            theme = 1
        else:
            theme = 0
        if request.POST['sorted_by'] == 'Title':
            sort_by = 'title'
        elif request.POST['sorted_by'] == 'Priority':
            sort_by = 'priority'
        else:
            sort_by = 'deadline'
        if 'clean_actions' in request.POST:
            Action.objects.all().delete()
        if 'clear_history' in request.POST:
            Task.objects.filter(status='Completed').delete()
        return redirect('task_list')
    context = {
        'title': 'Settings',
        'theme': theme,
        'form': form,
    }
    return render(request, 'main/index_settings.html', context)

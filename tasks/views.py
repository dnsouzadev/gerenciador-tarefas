from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task, Tag

@login_required
def list_task(request):
    tasks_filtered = Task.objects.filter(created_by=request.user)

    tags_da_tarefa = tasks_filtered[1].tags.all()
    print(tags_da_tarefa)


    context = {
        'tasks': tasks_filtered,
    }
    return render(request, 'list.html', context)

@login_required
def create_task(request):
    return render(request, 'create.html')

@login_required
def update_task(request, id):
    return render(request, 'update.html')

@login_required
def delete_task(request, id):
    return render(request, 'delete.html')

@login_required
def detail_task(request, id):
    return render(request, 'detail.html')

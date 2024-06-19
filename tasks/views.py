from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Tag
from .forms import TaskForm
from django.http import JsonResponse

@login_required
def list_task(request):
    tasks_filtered = Task.objects.filter(created_by=request.user)

    context = {
        'tasks': tasks_filtered,
    }
    return render(request, 'list.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            form.save_m2m()
            return redirect('list_task')
    else:
        form = TaskForm()
        return render(request, 'create.html', {'form': form})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    if not task:
        return redirect('list_task')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm(instance=task)
        return render(request, 'update.html', {'form': form})

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if task:
        task.delete()
    return JsonResponse({'status': 'ok'})

@login_required
def detail_task(request, id):
    task = Task.objects.get(id=id)
    if not task:
        return redirect('list_task')
    return render(request, 'detail.html', {'task': task})


@login_required
def change_status(request, id):
    task = Task.objects.get(id=id)
    if task:
        task.completed = not task.completed
        task.save()
    return JsonResponse({'status': 'ok'})


@login_required
def search_task(request):
    query = request.GET.get('q')
    tasks_filtered = Task.objects.filter(title__icontains=query, created_by=request.user)

    return render(request, 'list.html', {'tasks': tasks_filtered})

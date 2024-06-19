from datetime import date, datetime
from tasks.models import Task
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Usuário ou senha inválidos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    tasks = Task.objects.filter(created_by=request.user)
    tasks_count = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pendent_tasks = tasks_count - completed_tasks

    date_t = date.today()
    tasks_today = 0

    for task in tasks:
        if task.due_date.date() == date_t:
            tasks_today += 1

    tasks_completed = 0
    for task in tasks:
        if task.due_date.date() == date_t and task.completed == True:
            tasks_completed += 1



    get_tasks_today_count = tasks_today
    get_tasks_today_completed = tasks_completed
    get_tasks_today_pendent = get_tasks_today_count - get_tasks_today_completed

    context = {
        'tasks_count': tasks_count,
        'completed_tasks': completed_tasks,
        'pendent_tasks': pendent_tasks,
        'get_tasks_today_count': get_tasks_today_count,
        'get_tasks_today_completed': get_tasks_today_completed,
        'get_tasks_today_pendent': get_tasks_today_pendent
    }

    return render(request, 'home.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
        print(user.photo.url)

    return render(request, 'update_profile.html', {'form': form})

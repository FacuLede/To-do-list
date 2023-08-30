from django.shortcuts import render, redirect, reverse
from .forms import Task_form 
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.

@login_required
def create_task(request) :
    if request.method == 'GET' :
        return render(request, 'task_form.html', {
            'form':Task_form
        })
    elif request.method == 'POST' :
        form = Task_form(request.POST)
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('tasks')

@login_required
def tasks(request) :
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull = True)
    return render(request, 'tasks.html',{'tasks':tasks})

@login_required
def completed_tasks(request) :
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull = False).order_by('-datecompleted')
    return render(request, 'tasks.html',{'tasks':tasks})

@login_required
def task_detail(request, id) :
    task = get_object_or_404(Task, pk=id, user = request.user)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def update(request, id) :
    if request.method == 'GET' :        
        task = get_object_or_404(Task, pk=id, user = request.user)
        form = Task_form(instance=task)
        return render (request, 'task_form.html', {'form': form})
    elif request.method == 'POST' :
        task = get_object_or_404(Task, pk=id, user = request.user)
        form = Task_form(request.POST or None, instance = task)
        data = {
            'form': form,
        } 
        if form.is_valid() :
            form.save()
            params = {'id': id}
            return redirect(reverse(f'task_detail', kwargs=params)) 
        else :
            return render(request, 'update', data)

@login_required
def completed_task(request, id) :
    task = get_object_or_404(Task, pk=id, user = request.user)
    task.datecompleted = timezone.now()
    task.save()
    return redirect('tasks')
       
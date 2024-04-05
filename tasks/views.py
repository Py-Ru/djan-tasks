from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task', None)
        if task is not None:
            new_task = Task.objects.create(task=task)
            return redirect(reverse('index'))
    return render(request, 'tasks/add.html')

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')
    

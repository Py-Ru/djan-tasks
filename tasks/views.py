from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {'tasks':tasks})

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task', None)
        if task is not None:
            tasks.append(task)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'tasks/add.html', {'task': task})
    return render(request, 'tasks/add.html')
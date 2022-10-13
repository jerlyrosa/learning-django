from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.


def index(request):
    title = "Welcome to Django !!"
    return render(request, 'index.html', {
    'title': title
    })


def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = list(Project.objects.all())

    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request):
    # task = list(Task.objects.values())
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = list(Task.objects.all())

    return render(request, 'tasks.html',{
        'tasks': tasks
    })


def saludar(request, username):
    return HttpResponse(f'<h1>Hello {username}</h1>')



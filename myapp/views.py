from django.http import HttpResponse, JsonResponse

from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return HttpResponse("<h1>Index page</h1>")


def saludar(request, username):

    return HttpResponse(f'<h1>Hello {username}</h1>')


def about(request):
    return HttpResponse("<h1>About Vikingos</h1>")


def projects(request):
    projects = list(Project.objects.values());

    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # task = list(Task.objects.values())
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"<h1>Task: {task.title}</h1>")


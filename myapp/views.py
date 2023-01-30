from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = 'Django Practice!!'
    return render(request, 'index.html',{
        'title': title
    })


def about(request):
    username = 'lucas'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, id):
    result = id + 2 * 5
    return HttpResponse(f'<h1>Hello {result}</h1>')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {'projects' : projects})

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #task = Task.objects.get(title=title)
    #return HttpResponse(f'Task: {task.title}')
    return render(request, 'tasks.html')
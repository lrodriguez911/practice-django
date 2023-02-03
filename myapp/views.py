from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask

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
    tasks = Task.objects.all()
    #return HttpResponse(f'Task: {task.title}')
    return render(request, 'tasks.html', {"tasks": tasks})

def create_task(request):
    print(request.GET['title'])
    print(request.GET['description'])
    Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id=1)
    return render(request, 'create_task.html', {
        'form': CreateNewTask
    })
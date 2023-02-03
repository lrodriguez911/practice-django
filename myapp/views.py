from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewForm

# Create your views here.


def index(request):
    title = 'Django Practice!!'
    return render(request, 'index.html', {
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
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {'projects': projects})


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    # return HttpResponse(f'Task: {task.title}')
    return render(request, 'tasks/tasks.html', {"tasks": tasks})


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask
        })
    else:
        print(request.POST['project_id'])
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=request.POST['project_id'])
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewForm
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : tasks
    })
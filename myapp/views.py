from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, id):
    result = id + 2 * 5
    
    return HttpResponse(f'<h1>Hello {result}</h1>')

def about(request):
    return HttpResponse('<h2>About</h2>')
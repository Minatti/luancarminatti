from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def books(request):
    return render(request, 'books/books.html')

def resume(request):
    return render(request, 'resume.html')
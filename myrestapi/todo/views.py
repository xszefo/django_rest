from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# Create your views here.

class TodoList(ListView):
    queryset = Task.objects.all()
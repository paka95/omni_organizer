from django.shortcuts import render
from .apps import NotesConfig

# Create your views here.

app_name = NotesConfig.name

def index(request):
    return render(request, 'notes/index.html')
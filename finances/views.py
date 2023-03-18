from django.shortcuts import render
from .apps import FinancesConfig

# Create your views here.

app_name = FinancesConfig.name

def index(request):
    return render(request, 'finances/index.html')
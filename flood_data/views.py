from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'flood_data/main_dash.html')

from django.shortcuts import render
from .models import investment
# Create your views here.
def home(request):
    return render(request, 'home.html')
def funding(request):
    return render(request, 'funding.html')
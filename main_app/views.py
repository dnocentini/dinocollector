from django.shortcuts import render
from .models import Dino

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
    dinos = Dino.objects.all()
    return render(request, 'dinos/index.html', { 'dinos': dinos })

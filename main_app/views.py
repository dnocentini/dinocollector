from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Dino


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
    dinos = Dino.objects.all()
    return render(request, 'dinos/index.html', {'dinos': dinos})


def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    return render(request, 'dinos/detail.html', {'dino': dino})

class DinoCreate(CreateView):
  model = Dino
  fields = '__all__'
  

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dino
from .forms import FeedingForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
    dinos = Dino.objects.all()
    return render(request, 'dinos/index.html', {'dinos': dinos})


def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    feeding_form = FeedingForm()
    return render(request, 'dinos/detail.html', {
        'dino': dino, 'feeding_form': feeding_form
    })

def add_feeding(request, dino_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dino_id = dino_id
    new_feeding.save()
  return redirect('detail', dino_id=dino_id)   

class DinoCreate(CreateView):
  model = Dino
  fields = '__all__'

class DinoUpdate(UpdateView):
  model = Dino
  fields = ['nickname', 'description']

class DinoDelete(DeleteView):
  model = Dino
  success_url = '/dinos/'  
  

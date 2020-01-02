from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

import uuid
import boto3
from .models import Dino, Rock, Photo

class DinoCreate(CreateView):
    model = Dino
    fields = ['name', 'nickname', 'description', 'era']

class DinoUpdate(UpdateView):
    model = Dino
    fields = ['nickname', 'description']

class DinoDelete(DeleteView):
    model = Dino
    success_url = '/dinos/' 

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
    dinos = Dino.objects.all()
    return render(request, 'dinos/index.html', {'dinos': dinos})


def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    rocks_dino_doesnt_have = Rock.objects.exclude(id__in = dino.rocks.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dinos/detail.html', {
        'dino': dino, 'feeding_form': feeding_form,
        'rocks': rocks_dino_doesnt_have
    })

def add_feeding(request, dino_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dino_id = dino_id
        new_feeding.save()
    return redirect('detail', dino_id=dino_id) 

def assoc_rock(request, dino_id, rock_id):
    Dino.objects.get(id=dino_id).rocks.add(rock_id)
    return redirect('detail', dino_id=dino_id)  

def unassoc_rock(request, dino_id, rock_id):
    Dino.objects.get(id=dino_id).rocks.remove(rock_id)
    return redirect('detail', dino_id=dino_id)         


class RockList(ListView):
    model = Rock

class RockDetail(DetailView):
    model = Rock

class RockCreate(CreateView):
    model = Rock
    fields = '__all__'

class RockUpdate(UpdateView):
    model = Rock
    fields = ['name', 'color']

class RockDelete(DeleteView):
    model = Rock
    success_url = '/rocks/'

def add_photo(request, dino_id):
    S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
    BUCKET = 'dinocollector'
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, dino_id=dino_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', dino_id=dino_id)


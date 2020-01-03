from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Dino, Rock, Photo
from .forms import FeedingForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class DinoCreate(LoginRequiredMixin, CreateView):
    model = Dino
    fields = ['name', 'nickname', 'description', 'era']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DinoUpdate(LoginRequiredMixin, UpdateView):
    model = Dino
    fields = ['nickname', 'description']

class DinoDelete(LoginRequiredMixin, DeleteView):
    model = Dino
    success_url = '/dinos/' 

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def dinos_index(request):
    dinos = Dino.objects.filter(user=request.user)
    return render(request, 'dinos/index.html', {'dinos': dinos})

@login_required
def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    rocks_dino_doesnt_have = Rock.objects.exclude(id__in = dino.rocks.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dinos/detail.html', {
        'dino': dino, 'feeding_form': feeding_form,
        'rocks': rocks_dino_doesnt_have
    })

@login_required
def add_feeding(request, dino_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dino_id = dino_id
        new_feeding.save()
    return redirect('detail', dino_id=dino_id) 

@login_required
def assoc_rock(request, dino_id, rock_id):
    Dino.objects.get(id=dino_id).rocks.add(rock_id)
    return redirect('detail', dino_id=dino_id)  

@login_required
def unassoc_rock(request, dino_id, rock_id):
    Dino.objects.get(id=dino_id).rocks.remove(rock_id)
    return redirect('detail', dino_id=dino_id)         


class RockList(LoginRequiredMixin, ListView):
    model = Rock

class RockDetail(LoginRequiredMixin, DetailView):
    model = Rock

class RockCreate(LoginRequiredMixin, CreateView):
    model = Rock
    fields = '__all__'

class RockUpdate(LoginRequiredMixin, UpdateView):
    model = Rock
    fields = ['name', 'color']

class RockDelete(LoginRequiredMixin, DeleteView):
    model = Rock
    success_url = '/rocks/'

@login_required
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


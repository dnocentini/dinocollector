from django.shortcuts import render
from django.http import HttpResponse


class Dino:
    def __init__(self, name, nickname, description, era):
        self.name = name
        self.nickname = nickname
        self.description = description
        self.era = era


dinos = [
    Dino('Stegosaurus', 'Stego',
         'This slow-moving plant-eater used spikes on its tail to fend off would-be predators.', 'Late Jurassic Period'),
    Dino('Triceratops', 'Trike',
         'This plant-eater used its horns for defending itself from predators.', 'Late Cretaceous Period'),
    Dino('Tyrannosaurus', 'Carl', 'This infamous meat-eating predator, walked on two legs, balancing its huge head with a long and heavy tail that sometimes contained over 40 vertebrae.', 'Late Cretaceous Period')
]


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
    return render(request, 'dinos/index.html', {
        'dinos': dinos
    })

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dinos/', views.dinos_index, name='index'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='detail'),
    path('dinos/create/', views.DinoCreate.as_view(), name='dinos_create'),
]
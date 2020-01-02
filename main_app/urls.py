from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dinos/', views.dinos_index, name='index'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='detail'),
    path('dinos/create/', views.DinoCreate.as_view(), name='dinos_create'),
    path('dinos/<int:pk>/update/', views.DinoUpdate.as_view(), name='dinos_update'),
    path('dinos/<int:pk>/delete/', views.DinoDelete.as_view(), name='dinos_delete'),
    path('dinos/<int:dino_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dinos/<int:dino_id>/assoc_rock/<int:rock_id>/', views.assoc_rock, name='assoc_rock'),
    path('rocks/', views.RockList.as_view(), name='rocks_index'),
    path('rocks/<int:pk>/', views.RockDetail.as_view(), name='rocks_detail'),
    path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
    path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
    path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
]
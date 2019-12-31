from django.db import models

# Create your models here.

class Dino(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    era = models.CharField(max_length=100)

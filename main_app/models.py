from django.db import models
from django.urls import reverse

# Create your models here.

class Dino(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    era = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dino_id': self.id})    
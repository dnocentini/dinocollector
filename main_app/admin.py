from django.contrib import admin
from .models import Dino, Feeding, Rock

# Register your models here.
admin.site.register(Dino)
admin.site.register(Feeding)
admin.site.register(Rock)
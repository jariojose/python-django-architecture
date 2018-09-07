from django.contrib import admin
from .models import Notebook, Storage, CPU, Ram

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Storage)
admin.site.register(CPU)
admin.site.register(Ram)
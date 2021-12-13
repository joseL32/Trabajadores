from typing import List
from django.contrib import admin
from .models import Trabajador

class TrabajadorAdmin(admin.ModelAdmin):
    list_display =('id', 'nombres', 'dni', 'celular', 'direccion', 'especialidad')

admin.site.register(Trabajador,TrabajadorAdmin)


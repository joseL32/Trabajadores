from rest_framework import serializers
from .models import Trabajador

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Trabajador
        fields=('id', 'nombres', 'dni', 'celular', 'direccion', 'especialidad')

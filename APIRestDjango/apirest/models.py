from django.db import models

# Create your models here.

class Trabajador(models.Model):
    nombres=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=20, null=True)
    direccion=models.CharField(max_length=50)
    especialidad=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    area=models.CharField(max_length=30)
    

    class Meta:
        verbose_name = ("Trabajador")
        verbose_name_plural = ("Trabajadores")

    def __str__(self):
        return self.nombres

   
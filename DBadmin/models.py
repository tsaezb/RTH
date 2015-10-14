from django.db import models

class Paciente(models.Model):
    nombre= models.CharField(max_length=200)
    rut= models.CharField(max_length=10)
    sexo= models.CharField(max_length=1)
    fecha_nac= models.DateField('Fecha de Nacimiento')

    
# Create your models here.

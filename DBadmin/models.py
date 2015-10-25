from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nombre= models.CharField(max_length=200)
    rut= models.CharField(max_length=10)
    sexo= models.CharField(max_length=1)
    fecha_nac= models.DateField('Fecha de Nacimiento')

    
# Create your models here.

class Evento(models.Model):
    tipo_de_evento_opciones= (('PreTX','PreTransplante'),
                               ('TX','Transplante'),
                               ('PostTX','PostTransplante'),
                              )
    tipo= models.CharField(max_length=100,choices=tipo_de_evento_opciones)
    fecha= models.DateField('Fecha del Evento',default=timezone.now)

class Transplante(Evento):
    situacion_opciones= (('Electivo','Electivo'),
                               ('Urgencia1','Urgencia Tipo1'),
                               ('Urgencia2','Urgencia Tipo2'),
                               ('Urgencia3','Urgencia Tipo3'),
                              )
    diagnostico= models.CharField(max_length=100)
    causa_enlistamiento= models.CharField(max_length=100)
    situacion= models.CharField(max_length=30,choices=situacion_opciones)
    antecedentes_previos=models.ManyToManyField(AntecedentePretransplante)

class AntecedentePretransplante(models.Model):
    nombre= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Antecedentes Pretransplante"
    def __str__(self):
        return self.nombre
    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)
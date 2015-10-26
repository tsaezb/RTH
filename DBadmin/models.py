from django.db import models
from django.utils import timezone


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Enfermedades"
    def __str__(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Habito(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    servicio_salud = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Hospitales"

    def __str__(self):
        return self.nombre + ", " + self.servicio_salud

    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Paciente(models.Model):
    #datos personales
    nombre= models.CharField(max_length=200)
    rut= models.CharField(max_length=10)

    op_sexo=    (('m','Masculino'),
                 ('f','Femenino'))
    sexo= models.CharField(max_length=1,choices=op_sexo,null=True)
    fecha_nac= models.DateField('Fecha de Nacimiento')

    #direccion
    direccion = models.CharField(max_length=200,null=True)
    comuna = models.ForeignKey(Comuna,null=True)

    #datos salud
    hospital = models.ForeignKey(Hospital,null=True)
    op_prevision =   (('fon', 'FONASA'),
                 ('isa', 'ISAPRE'),)
    prevision = models.CharField(max_length=10,choices=op_prevision,null=True)

    op_grupo_sang=  (('o+','O Rh+'),
                     ('a+','A Rh+'),
                     ('b+','B Rh+'),
                     ('ab+','AB Rh+'),
                     ('o-','O Rh-'),
                     ('a-','A Rh-'),
                     ('b-','B Rh-'),
                     ('ab-','AB Rh-'),)
    grupo_sang = models.CharField(max_length=3,choices=op_grupo_sang,null=True)

    #antecedentes
    enfermedades_previas= models.ManyToManyField(Enfermedad)
    antecedentes_quirurgicos = models.NullBooleanField()
    habitos = models.ManyToManyField(Habito)


class Evento(models.Model):
    tipo_de_evento_opciones= (('PreTX','PreTransplante'),
                               ('TX','Transplante'),
                               ('PostTX','PostTransplante'),
                              )
    tipo= models.CharField(max_length=100,choices=tipo_de_evento_opciones)
    fecha= models.DateField('Fecha del Evento',default=timezone.now)


class AntecedentePretransplante(models.Model):
    nombre= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Antecedentes Pretransplante"
    def __str__(self):
        return self.nombre
    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Pretransplante(Evento):
    situacion_opciones= (('Electivo','Electivo'),
                               ('Urgencia1','Urgencia Tipo1'),
                               ('Urgencia2','Urgencia Tipo2'),
                               ('Urgencia3','Urgencia Tipo3'),
                              )
    diagnostico= models.CharField(max_length=100)
    causa_enlistamiento= models.CharField(max_length=100)
    situacion= models.CharField(max_length=30,choices=situacion_opciones)
    antecedentes_previos=models.ManyToManyField(AntecedentePretransplante)

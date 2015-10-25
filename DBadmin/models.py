from django.db import models

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

class Paciente(models.Model):
    nombre= models.CharField(max_length=200)
    rut= models.CharField(max_length=10)
    sexo= models.CharField(max_length=1)
    fecha_nac= models.DateField('Fecha de Nacimiento')

    direccion = models.CharField(max_length=200,null=True)
    #comuna = models.ForeignKey(Comuna)
    #hospital = models.ForeignKey(Hospital)
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

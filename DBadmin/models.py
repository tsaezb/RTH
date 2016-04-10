from django.db import models
from django.utils import timezone


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


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

    def __str__(self):
        return self.nombre + ", " + self.rut


class Evento(models.Model):
    tipo_de_evento_opciones= (('PreTX','PreTrasplante'),
                               ('TX','Trasplante'),
                               ('PostTX','PostOperatorio'),
                               ('Compl','Complicacion'),
                               ('ReHos','Rehospitalizacion'),
                               ('Lab','Laboratorio'),
                               ('Don','Donante'),
                              )
    paciente= models.ForeignKey(Paciente,null=True)
    tipo= models.CharField(max_length=100,choices=tipo_de_evento_opciones)
    fecha= models.DateField('Fecha del Evento',default=timezone.now)


class AntecedentePretrasplante(models.Model):
    nombre= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Antecedentes Pretrasplante"
    def __str__(self):
        return self.nombre
    @staticmethod
    def autocomplete_search_fields():
        return ("nombre__iexact","nombre__icontains",)


class Pretrasplante(Evento):

    diagnostico= models.CharField(max_length=100)
    causa_enlistamiento= models.CharField(max_length=100)
    situacion_opciones =    (('Electivo','Electivo'),
                             ('Urgencia1','Urgencia Tipo1'),
                             ('Urgencia2','Urgencia Tipo2'),
                             ('Urgencia3','Urgencia Tipo3'),)
    situacion= models.CharField(max_length=30,choices=situacion_opciones)
    antecedentes_previos= models.ManyToManyField(AntecedentePretrasplante)
    fecha_enlistamiento= models.DateField(default=timezone.now)
    peso= models.FloatField(default=0)
    estatura= models.IntegerField(default=0)
    score_child= models.FloatField(default=0)
    factor_de_reajuste_childpugh= models.FloatField(default=0)
    score_meld= models.FloatField(default=0)

    def save(self):
        self.tipo= "PreTX"
        super(Pretrasplante, self).save()


class Trasplante(Evento):
    fecha_operacion = models.DateField(default=timezone.now)
    score_child= models.FloatField(default=0)
    factor_de_reajuste_childpugh= models.FloatField(default=0)
    score_meld= models.FloatField(default=0)
    situacion_opciones =    (('Electivo','Electivo'),
                             ('Urgencia1','Urgencia Tipo1'),
                             ('Urgencia2','Urgencia Tipo2'),
                             ('Urgencia3','Urgencia Tipo3'),)
    situacion= models.CharField(max_length=30,choices=situacion_opciones)
    #serologia

    #tratamiento organo
    solucion_opciones = (('solucion1','Solucion 1'),
                        ('solucion2','Solucion 2'),
                        ('solucion3','Solucion 3'),)
    tipo_solucion = models.CharField(max_length=30,choices=solucion_opciones)
    distribucion_opciones = (('via1','Via 1'),
                            ('via2','Via 2'),
                            ('via3','Via 3'),)
    distribucion_solucion = models.CharField(max_length=30,choices=solucion_opciones)

    porcentaje_esteatosis = models.FloatField(default=0)

    #operacion
    tiempo_total = models.IntegerField(default=0)
    izquemia_fria = models.IntegerField(default=0)
    izquemia_caliente = models.IntegerField(default=0)

    tecnica_opciones = (('tecnica1','Tecnica 1'),
                            ('tecnica2','Tecnica 2'),
                            ('tecnica3','Tecnica 3'),)
    tecnica = models.CharField(max_length=30,choices=tecnica_opciones)
    #transfusiones

    def save(self):
        self.tipo = "TX"
        super(Trasplante, self).save()


class Postoperatorio(Evento):
    #Hospitalizacion
    dias_totales = models.IntegerField(default=0)
    dias_uci = models.IntegerField(default=0)
    horas_ventilacion_mecanica = models.IntegerField(default=0)
    dias_soporte_renal = models.IntegerField(default=0)

    #Explante
    hcc = models.NullBooleanField()
    peso = models.FloatField(default=0)
    datos_interes = models.TextField(max_length=500,default="")

    def save(self):
        self.tipo = "PostTX"
        super(Postoperatorio, self).save()


class Complicacion(Evento):

    class Meta:
        verbose_name_plural = "Complicaciones"

    op_tipo_complicacion = (('rech','Rechazo'),
                            ('vasc','Vascular'),
                            ('bili','Biliar'),
                            ('infe','Infeccion'),
                            ('neur','Neurologica'),
                            ('neop','Neoplasica'),
                            ('card','Cardiovascular'),
                            ('enfb','Reaparicion enfermedad base'),)
    tipo_complicacion = models.CharField(max_length=4,choices=op_tipo_complicacion)
    fecha_complicacion = models.DateField(default=timezone.now)
    operacion = models.NullBooleanField()
    tratamiento = models.TextField(max_length=500,default="")
    detalles = models.TextField(max_length=500,default="")

    def save(self):
        self.tipo = "Compl"
        super(Complicacion, self).save()


class Rehospitalizacion(Evento):

    fecha_rehospitalizacion = models.DateField(default=timezone.now)
    causa_rehospitalizacion = models.TextField(max_length=500,default="")

    def save(self):
        self.tipo = "ReHos"
        super(Rehospitalizacion, self).save()


class Laboratorio(Evento):

    fecha_lab = models.DateField(default=timezone.now)

    #resultados
    got = models.FloatField(default=0)
    gpt = models.FloatField(default=0)
    fa = models.FloatField(default=0)
    ggt = models.FloatField(default=0)
    bilis_total = models.FloatField(default=0)
    bilis_dir = models.FloatField(default=0)
    inr = models.FloatField(default=0)

    def save(self):
        self.tipo = "Lab"
        super(Laboratorio, self).save()


class Donante(Evento):

    #datos personales
    nombre= models.CharField(max_length=200)
    rut= models.CharField(max_length=10)

    op_sexo=    (('m','Masculino'),
                 ('f','Femenino'))
    sexo= models.CharField(max_length=1,choices=op_sexo,null=True)
    edad = models.IntegerField(default=0)

    #datos salud
    peso = models.IntegerField(default=0)
    talla = models.IntegerField(default=0)
    hospital = models.ForeignKey(Hospital,null=True)
    op_grupo_sang=  (('o+','O Rh+'),
                     ('a+','A Rh+'),
                     ('b+','B Rh+'),
                     ('ab+','AB Rh+'),
                     ('o-','O Rh-'),
                     ('a-','A Rh-'),
                     ('b-','B Rh-'),
                     ('ab-','AB Rh-'),)
    grupo_sang = models.CharField(max_length=3,choices=op_grupo_sang,null=True)

    #datos organo
    injerto_opciones = (('injerto1','Injerto 1'),
                        ('injerto2','Injerto 2'),
                        ('injerto3','Injerto 3'),)
    tipo_injerto = models.CharField(max_length=3,choices=injerto_opciones)

    #serologia
    #pruebas de Lab

    bar_score = models.FloatField(default=0)
    vivo_muerto = models.NullBooleanField()

    def save(self):
        self.tipo = "Don"
        super(Donante, self).save()

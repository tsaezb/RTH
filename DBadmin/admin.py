from django.contrib import admin

from .models import *

#plas plas

admin.site.register(Paciente)
admin.site.register(Enfermedad)
admin.site.register(Habito)
admin.site.register(Pretransplante)
admin.site.register(AntecedentePretransplante)

# Register your models here.

from django.contrib import admin

from .models import *


class PacienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Personales',        {'fields': ['nombre', 'rut', 'sexo', 'fecha_nac']}),
        ('Direccion',               {'fields': ['direccion', 'comuna']}),
        ('Datos Salud',             {'fields': ['grupo_sang', 'prevision', 'hospital']}),
        ('Antecedentes Salud',      {'fields': ['enfermedades_previas', 'antecedentes_quirurgicos', 'habitos']}),
    ]
    raw_id_fields = ('comuna','enfermedades_previas','hospital','habitos')
    autocomplete_lookup_fields = {'fk': ['comuna','hospital'], 'm2m': ['enfermedades_previas','habitos'],}


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Enfermedad)
admin.site.register(Habito)
admin.site.register(Comuna)
admin.site.register(Hospital)
admin.site.register(Pretransplante)
admin.site.register(AntecedentePretransplante)

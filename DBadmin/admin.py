from django.contrib import admin

from .models import *

class PretransplanteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['paciente',]}),
        ('Antropometria',   {'fields': ['estatura','peso',]}),
        ('Datos Medicos',   {'fields': ['fecha_enlistamiento','diagnostico','causa_enlistamiento','situacion','antecedentes_previos',]}),
        ('Scores',          {'fields': ['score_child','factor_de_reajuste_childpugh','score_meld',]})
        ]
    list_display = ('paciente','tipo','fecha','score_child','factor_de_reajuste_childpugh','score_meld',)
    list_filter = ['paciente']
    search_fields = ['paciente']
    raw_id_fields = ('paciente','antecedentes_previos')
    autocomplete_lookup_fields = {'m2m': ['antecedentes_previos'],'fk': ['paciente'],}


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
admin.site.register(Pretransplante,PretransplanteAdmin)
admin.site.register(AntecedentePretransplante)

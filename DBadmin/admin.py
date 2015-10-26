from django.contrib import admin

from .models import *

class PretransplanteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['paciente','diagnostico',]}),
        ('Antropometria',{'fields':['estatura','peso',]})
        ('Datos Medicos',{'fields':['fecha_enlistamiento','diagnostico','causa_enlistamiento','situacion','antecedentes_previos',]}),
        ('Scores',{'fields':['score_child','factor_de_reajuste_childpugh','score_meld',]})
        ]
    list_display = ('paciente','tipo','fecha','score_child','factor_de_reajuste_childpugh','score_meld',)
    list_filter = ['paciente']
    search_fields = ['paciente']
    raw_id_fields = ('paciente','antecedentes_previos')
    autocomplete_lookup_fields = {'m2m': ['antecedentes_previos'],'fk': ['paciente'],}

admin.site.register(Paciente)
admin.site.register(Enfermedad)
admin.site.register(Habito)
admin.site.register(Pretransplante,PretransplanteAdmin)
admin.site.register(AntecedentePretransplante)

# Register your models here.
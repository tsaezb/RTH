from django.contrib import admin

from .models import *

class PretransplanteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['paciente','fecha','diagnostico','causa_enlistamiento','situacion','antecedentes_previos']}),
        ]
    list_display = ('paciente','tipo','fecha',)
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
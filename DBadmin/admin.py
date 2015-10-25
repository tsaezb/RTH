from django.contrib import admin

from .models import *

<<<<<<< HEAD
admin.site.register(Paciente)
admin.site.register(Enfermedad)
admin.site.register(Habito)
=======
class AntecedentePretransplanteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre']}),
        ]
    search_fields = ['nombre']
    raw_id_fields = ('nombre')
    autocomplete_lookup_fields = {'m2m': ['nombre'],}

>>>>>>> origin/master

admin.site.register(Paciente
admin.site.register(Enfermedad)
admin.site.register(AntecedentePretransplante,AntecedentePretransplanteAdmin)

# Register your models here.

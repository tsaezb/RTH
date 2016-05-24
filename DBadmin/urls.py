from django.conf.urls import patterns, url
from DBadmin import views

urlpatterns = patterns('',
    url(r'^user.json', views.userdata, name='userdata'),
    url(r'^comunas.json', views.comunas, name='comunas'),
    url(r'^hospitales.json', views.hospitales, name='hospitales'),
    url(r'^grupos-sanguineos.json', views.gruposSanguineos, name='gruposSanguineos'),
    url(r'^habitos.json', views.habitos, name='habitos'),
    url(r'^enfermedades.json', views.enfermedades, name='enfermedades'),
    url(r'^previsiones.json', views.previsiones, name='previsiones'),
    url(r'^lookup/pacientes.json', views.pacientesLookup, name="pacientesLookup"),
#    url(r'^busqueda-persona/$', views.searchByPerson, name='searchByPerson'),z
)

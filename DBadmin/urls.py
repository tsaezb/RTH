from django.conf.urls import patterns, url
from DBadmin import views

urlpatterns = patterns('',
    url(r'^user.json', views.userdata, name='userdata'),
    url(r'^comunas.json', views.comunas, name='comunas'),
    url(r'^hospitales.json', views.hospitales, name='hospitales'),
    url(r'^grupos-sanguineos.json', views.gruposSanguineos, name='gruposSanguineos'),
#    url(r'^busqueda-persona/$', views.searchByPerson, name='searchByPerson'),z
)

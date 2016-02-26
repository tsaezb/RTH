from django.conf.urls import patterns, url
from DBadmin import views

urlpatterns = patterns('',
    url(r'^user.json', views.userdata, name='userdata'),
#    url(r'^busqueda-persona/$', views.searchByPerson, name='searchByPerson'),z
)

from django.conf.urls import patterns, url
from server import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
#    url(r'^busqueda-persona/', views.searchByPerson, name='searchByPerson'),z
)

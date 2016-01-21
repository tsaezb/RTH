from django.conf.urls import patterns, url
from DBadmin import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
#    url(r'^busqueda-persona/', views.searchByPerson, name='searchByPerson'),
)

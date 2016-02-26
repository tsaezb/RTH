"""RTH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', include('DBadmin.urls')), # serves DB interactions
    url(r'^$', include('server.urls')), # serves main page
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static('/bower_components/', document_root='static/bower_components/'
) + static('/css/', document_root='static/css/'
#) + static('/data/', document_root='static/data/'
) + static('/fonts/', document_root='static/fonts/'
) + static('/img/', document_root='static/img/'
) + static('/js/', document_root='static/js/'
) + static('/less/', document_root='static/less/'
) + static('/media/', document_root='static/media/'
) + static('/template/', document_root='static/template/'
) + static('/vendors/', document_root='static/vendors/'
) + static('/views/', document_root='static/views/'
)


#Sistema de Login

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='rth_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='rth_logout'),
)

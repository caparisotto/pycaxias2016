"""palestra URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', 'pycaxias2016.views.inicial'),
    url(r'^slide2/', 'pycaxias2016.views.slide2'),
    url(r'^slide3/', 'pycaxias2016.views.slide3'),
    url(r'^slide4/', 'pycaxias2016.views.slide4'),
    url(r'^slide5/', 'pycaxias2016.views.slide5'),
    url(r'^slide6/', 'pycaxias2016.views.slide6'),
    url(r'^slide7/', 'pycaxias2016.views.slide7'),
    url(r'^slide8/', 'pycaxias2016.views.slide8'),
    url(r'^slide9/', 'pycaxias2016.views.slide9'),
    url(r'^slide10/', 'pycaxias2016.views.slide10'),
    url(r'^slide11/', 'pycaxias2016.views.slide11'),
    url(r'^slide12/', 'pycaxias2016.views.slide12'),
    url(r'^slide13/', 'pycaxias2016.views.slide13'),
    url(r'^end/', 'pycaxias2016.views.final'),

#    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
        urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )
                

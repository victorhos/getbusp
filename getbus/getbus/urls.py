from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'getbus.views.home', name='home'),

    url(r'^auth_sptrans/$', 'getbus.views.auth_sptrans', name='auth_sptrans'),

    url(r'^buscar_bus/$', 'getbus.views.buscar_bus', name='buscar_bus'),
    url(r'^detalhe_bus/$', 'getbus.views.detalhe_bus', name='detalhe_bus'),
    url(r'^paradas_bus/$', 'getbus.views.paradas_bus', name='paradas_bus'),

    url(r'^admin/', include(admin.site.urls)),
)

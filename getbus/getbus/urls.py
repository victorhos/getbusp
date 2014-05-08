from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'getbus.views.home', name='home'),
    url(r'^auth_sptrans/$', 'getbus.views.auth_sptrans', name='auth_sptrans'),

    url(r'^admin/', include(admin.site.urls)),
)

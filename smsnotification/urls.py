from django.conf.urls import patterns, include, url
from django.contrib import admin
import django_cron

django_cron.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hospitalUser/', include('portal.urls')),
    url(r'^', include('public.urls')),    
)

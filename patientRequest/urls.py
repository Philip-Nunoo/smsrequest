from django.conf.urls import patterns, include, url
from django.contrib import admin
import django_cron

django_cron.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Url to app installed
    url(r'^project/', include('patientProject.urls')),
    url(r'^hospitalUser/', include('patientProject.urls_user')),
)

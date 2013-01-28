from django.conf.urls import patterns, url

urlpatterns = patterns('patientProject.views',
    url(r'^$','index', name='index'),
    
    url(r'^login','loginUser', name='loginUser'),
    url(r'^register','registerUser', name='registerUser'),
    url(r'^logout','logoutUser', name='logoutUser')
)
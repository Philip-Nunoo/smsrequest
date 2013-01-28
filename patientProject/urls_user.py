from django.conf.urls import patterns, url

urlpatterns = patterns('patientProject.views_user',
    url(r'^$','index', name='index'),
    url(r'^createNewMessage', 'createNewMessage', name='newMessage'),
    url(r'^addNewPatient', 'addNewPatient', name='newPatient'),
    url(r'^addPersonnel', 'addPersonnel', name='addPersonnel'),
    url(r'^viewLog','viewLog',name='viewLog'),
    
)
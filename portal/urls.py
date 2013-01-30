from django.conf.urls import patterns, url

urlpatterns = patterns('portal.views',	
    url(r'^$', 'home', name='home'),
    url(r'^createNewMessage', 'createNewMessage', name='newMessage'),
    url(r'^addNewPatient', 'addNewPatient', name='newPatient'),
    url(r'^addPersonnel', 'addPersonnel', name='newPersonnel'),
    url(r'^viewMessages', 'viewMessages', name='viewMessages'),
    url(r'^viewPatients', 'viewPatients', name='viewPatients'),
    url(r'^viewPersonnels', 'viewPersonnels', name='viewPersonnels'),
    url(r'^viewLog','viewLog',name='viewLog'),
)

from django.conf.urls import patterns,url

urlpatterns = patterns('public.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^register','register', name='register'),
    url(r'^login','login_user', name='login'),
    url(r'^logout','logout_user', name='logout'),
)

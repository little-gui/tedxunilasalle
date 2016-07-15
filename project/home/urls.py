from django.conf.urls import patterns, url

from home import views


urlpatterns = [ 
    url(r'^$', views.index, name='home'),
    url(r'^contato/?$', views.contact, name='contact')
]

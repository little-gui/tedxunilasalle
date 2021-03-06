from django.conf.urls import patterns, url

from blog import views


urlpatterns = [ 
    url(r'^$', views.home, name='blog_home'),
    url(r'^(?P<post_id>[\d]+)/(?P<slug>[\S]+)/?$', views.post, name='blog_post'),
]

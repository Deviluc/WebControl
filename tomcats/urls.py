from django.conf.urls import url

from . import views

app_name = 'tomcats'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^instances/(?P<tomcat_instance_id>[0-9]+)/$', views.details, name='details'),
]
from django.conf.urls import url

from . import views

app_name = 'base'

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^jobs/$', views.jobs_overview, name='jobs_overview'),
    url(r'^scripts/$', views.scripts_overview, name='scripts_overview'),
    url(r'', views.index, name='index_redirect')
]
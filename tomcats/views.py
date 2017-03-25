from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.template import loader

from .models import TomcatInstance, Server, TomcatGroup

# Create your views here.
def index(request):
	tomcat_instance_list = TomcatInstance.objects.all()
	tomcat_group_list = TomcatGroup.objects.all()
	server_list = Server.objects.all()
	context = {
		'tomcat_instance_list': tomcat_instance_list,
		'tomcat_group_list': tomcat_group_list,
		'server_list': server_list,
		'filter_server': server_list[0],
		'filter_group': None,
	}

	return render(request, 'instances/index.html', context)


def details(request, tomcat_instance_id):
	instance = get_object_or_404(TomcatInstance, pk=tomcat_instance_id)
	return HttpResponse("You're viewing tomcat instance with id %s" %instance.id)
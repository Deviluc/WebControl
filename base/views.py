from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.template import loader

from .models import Script, ExecutionEnvironment


# Create your views here.
def index(request):
	return render(request, 'core/home.html', {})

def jobs_overview(request):

	return render(request, 'jobs/overview.html', {})

def scripts_overview(request):
	selectedEnv = None
	scripts = Script.objects.all()

	try:
		selectedEnv = request.POST['environment']
		scripts = [script for script in scripts if script.executionEnvironment == selectedEnv]
	except (KeyError):
		()

	return render(request, 'scripts/overview.html', {'environments': ExecutionEnvironment.objects.all(), 'selected-environment': selectedEnv, 'scripts': scripts})
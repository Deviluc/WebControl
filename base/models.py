import string
import random
from django.db import models

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def user_dir_path():
	return ""

def script_file_path(instance, filename):
	return 'scripts/{0}_{1}'.format(id_generator(), filename)

class ExecutionEnvironment(models.Model):
	name = models.CharField(max_length=100)
	version = models.CharField(max_length=100)
	executablePath = models.CharField(max_length=1000)

	def __str__(self):
		return self.name + " - " + self.version

# Create your models here.
class Script(models.Model):
	name = models.CharField(max_length=200)
	executionEnvironment = models.ForeignKey(ExecutionEnvironment, on_delete=models.DO_NOTHING)
	scriptFile = models.FileField(upload_to=script_file_path)

	def __str__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length=200)
	script = models.ForeignKey(Script, on_delete=models.DO_NOTHING)
	arguments = models.TextField(blank=True)

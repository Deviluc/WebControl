from django.db import models

# Create your models here.
class Server(models.Model):
	display_name = models.CharField(max_length=100)
	ip_host_name = models.CharField(max_length=200, unique=True)
	is_ip = models.BooleanField(default=True)

	def __str__(self):
		return self.display_name

class Credential(models.Model):
	username = models.CharField(max_length=200)
	private_key = models.CharField(max_length=4000)
	server = models.ForeignKey(Server, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.username + "@" + self.server.ip_host_name

class TomcatGroup(models.Model):
	number = models.IntegerField()
	description = models.TextField(blank=True)
	description_html = models.BooleanField(default=False)
	server = models.ForeignKey(Server, on_delete=models.DO_NOTHING)

	def __str__(self):
		return str(self.number)

class TomcatInstance(models.Model):
	number = models.IntegerField()
	display_name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	description_html = models.BooleanField(default=False)
	auto_refresh_build_info = models.BooleanField(default=True)
	build_info_refresh_interval = models.IntegerField(default=5, help_text="in minutes")
	tomcatGroup = models.ForeignKey(TomcatGroup, on_delete=models.DO_NOTHING)

	def __str__(self):
		return str(self.display_name)


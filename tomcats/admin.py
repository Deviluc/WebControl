from django.contrib import admin
from .models import Server, Credential, TomcatGroup, TomcatInstance

# Register your models here.
admin.site.register(Server)
admin.site.register(Credential)
admin.site.register(TomcatGroup)
admin.site.register(TomcatInstance)
from django.contrib import admin
from .models import ExecutionEnvironment, Script, Job

# Register your models here.
admin.site.register(ExecutionEnvironment)
admin.site.register(Script)
admin.site.register(Job)
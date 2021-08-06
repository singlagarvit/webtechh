from django.contrib import admin
from .models import Service, ServiceProcess

class ServiceProcessInline(admin.StackedInline):
	model = ServiceProcess
	extra = 0

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	inlines = [ServiceProcessInline, ]

class ServiceProcessAdmin(admin.ModelAdmin):
	list_display = ['title', 'service']

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceProcess, ServiceProcessAdmin)
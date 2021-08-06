from django.shortcuts import render, get_object_or_404
from .models import Service
from project.models import Project

def service(request, service_slug):
	service = get_object_or_404(Service, slug=service_slug)
	projects = Project.objects.filter(service=service, featured=True)
	context = {
		'service': service,
		'featured_projects': projects
	}
	return render(request, 'service/service.html', context)
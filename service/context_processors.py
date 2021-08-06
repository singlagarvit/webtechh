from .models import Service

def service(request):
	services = Service.objects.all()
	return {
		'services': services
	}
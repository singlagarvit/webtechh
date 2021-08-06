from django.contrib.sites.models import Site

def components(request):
	current_site = Site.objects.get_current()
	return {
		'current_site': current_site
	}
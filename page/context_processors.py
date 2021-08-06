from .models import FooterPage, StaticPage

def pages(request):
	footer_pages = FooterPage.objects.all()
	static_pages = StaticPage.objects.all()
	return {
		'footer_pages': footer_pages,
		'static_pages': static_pages
	}
from django.shortcuts import render
from .models import FooterPage, StaticPage

def page(request, page_slug):
	try:
		page = FooterPage.objects.get(slug=page_slug)
		context = {
			'page': page
		}
		return render(request, 'page/footer_page.html', context)
	except FooterPage.DoesNotExist:
		page = StaticPage.objects.get(slug=page_slug)
		context = {
			'page': page
		}
		return render(request, 'page/static_page.html', context)
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project, CaseStudy
from service.models import Service

def portfolio(request):
	services = Service.objects.all()
	projects = Project.objects.all()
	featured_projects = projects.filter(featured=True)
	context = {
		'services': services,
		'projects': projects,
		'featured_projects': featured_projects
	}
	return render(request, 'project/portfolio.html', context)

def studies(request):
	studies = CaseStudy.objects.all()
	paginator = Paginator(studies, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'studies': page_obj
	}
	return render(request, 'project/studies.html', context)

def case(request, case_slug):
	case = get_object_or_404(CaseStudy, slug=case_slug)
	context = {
		'case': case
	}
	return render(request, 'project/case.html', context)
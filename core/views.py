from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from urllib.parse import urlencode, urlparse
from .forms import QueryForm, SubscriptionForm
from .models import Subscription
from project.models import Project, CaseStudy
from service.models import Service
from component.models import HeroSlide
from blog.models import Post

def index(request):
	slides = HeroSlide.objects.all()
	projects = Project.objects.all()
	featured_case_studies = CaseStudy.objects.filter(featured=True)[0:3]
	latest_posts = Post.objects.all()[0:3]
	context = {
		'slides': slides,
		'projects': projects,
		'featured_case_studies': featured_case_studies,
		'latest_posts': latest_posts
	}
	return render(request, 'core/index.html', context)

@require_POST
def queries(request):
	form = QueryForm(request.POST)
	if form.is_valid():
		query = form.save()
		messages.success(request, f"Dear {query.name}, we have recieved your query! Our represntative will get back to you shortly.")
		return redirect('core:index')
	
	params = urlencode(request.POST)
	url_path = urlparse(request.META.get('HTTP_REFERER')).path
	response = redirect(url_path)
	response['Location'] += f'?{params}'
	return response

@require_POST
def subscribe(request):
	form = SubscriptionForm(request.POST)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		name = form.cleaned_data.get('name')
		try:
			subscription = Subscription.objects.get(email=email)
			messages.warning(request, f"Dear {name}, this email has already been registered. Please use another email.")
		except Subscription.DoesNotExist:
			subscription = form.save()
			messages.success(request, f"Dear {name}, you have successfully subscribed to the newsletter.")
		return redirect('core:index')
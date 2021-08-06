from django.urls import path
from .views import portfolio, studies, case

app_name = 'project'

urlpatterns = [
	path('portfolio/', portfolio, name='portfolio'),
	path('case-studies/', studies, name='studies'),
	path('case-studies/<slug:case_slug>/', case, name='case'),
]
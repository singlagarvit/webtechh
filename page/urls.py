from django.urls import path
from .views import page

app_name = 'page'

urlpatterns = [
	path('<slug:page_slug>/', page, name='page'),
]
from django.urls import path
from .views import index, queries, subscribe, contact
app_name = 'core'
urlpatterns = [
	path('', index, name='index'),
	path('get-a-quote/', queries, name='queries'),
	path('subscribe/', subscribe, name='subscribe'),
	path('contact-us/', contact, name='contact'),
]
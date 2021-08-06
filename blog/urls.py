from django.urls import path
from .views import blog, category, tag, post, search

app_name = 'blog'

urlpatterns = [
	path('', blog, name='blog'),
	path('search/', search, name='search'),
	path('category/<slug:category_slug>/', category, name='category'),
	path('tag/<slug:tag_slug>/', tag, name='tag'),
	path('post/<slug:post_slug>/', post, name='post'),
]
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Category, Tag, Author, Post, Comment
from .forms import CommentForm

def blog(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	recent_posts = posts[0:5]
	recent_comments = Comment.objects.all()[0:3]
	categories = Category.objects.all()[0:5]
	tags = Tag.objects.all()[0:7]

	context = {
		'posts': page_obj,
		'recent_posts': recent_posts,
		'recent_comments':recent_comments,
		'categories':categories,
		'tags':tags
	}
	return render(request, 'blog/blog.html', context)

def category(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	posts = Post.objects.filter(category=category)
	paginator = Paginator(posts, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	recent_posts = Post.objects.all()[0:5]
	recent_comments = Comment.objects.all()[0:3]
	categories = Category.objects.all()[0:5]
	tags = Tag.objects.all()[0:7]

	context = {
		'category': category,
		'posts': page_obj,
		'recent_posts': recent_posts,
		'recent_comments':recent_comments,
		'categories':categories,
		'tags':tags
	}
	return render(request, 'blog/category.html', context)

def tag(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	posts = Post.objects.filter(tags=tag)
	paginator = Paginator(posts, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	recent_posts = Post.objects.all()[0:5]
	recent_comments = Comment.objects.all()[0:3]
	categories = Category.objects.all()[0:5]
	tags = Tag.objects.all()[0:7]

	context = {
		'tag': tag,
		'posts': page_obj,
		'recent_posts': recent_posts,
		'recent_comments':recent_comments,
		'categories':categories,
		'tags':tags
	}
	return render(request, 'blog/tag.html', context)

def post(request, post_slug):
	post = get_object_or_404(Post, slug=post_slug)
	recent_posts = Post.objects.all()[0:5]
	recent_comments = Comment.objects.all()[0:3]
	categories = Category.objects.all()[0:5]
	tags = Tag.objects.all()[0:7]
	
	context = {
		'post': post,
		'recent_posts': recent_posts,
		'recent_comments':recent_comments,
		'categories':categories,
		'tags':tags
	}
	return render(request, 'blog/post.html', context)

def search(request):
	query = request.GET.get('q')
	queryset = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)| Q(category__title__icontains=query)).distinct()
	paginator = Paginator(queryset, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'query': query,
		'posts': page_obj
	}
	return render(request, 'blog/search.html', context)
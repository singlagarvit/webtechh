from django.contrib import admin
from .models import Category, Tag, Author, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']

class TagAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'category', 'author', 'created_on']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['post', 'name', 'email', 'timestamp', 'approved']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
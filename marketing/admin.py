from django.contrib import admin
from .models import SEOTag

class SEOTagAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(SEOTag, SEOTagAdmin)
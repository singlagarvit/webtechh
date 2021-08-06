from django.contrib import admin
from .models import FooterPage, StaticPage, PageSection

class PageSectionInline(admin.StackedInline):
	model = PageSection
	extra = 0

class FooterPageAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']

class StaticPageAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'tagline']
	inlines = [PageSectionInline, ]

class PageSectionAdmin(admin.ModelAdmin):
	list_display = ['page', 'title']

admin.site.register(FooterPage, FooterPageAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(PageSection, PageSectionAdmin)
from django.contrib import admin
from .models import HeroSlide, NumberCounter, Counter, Newsletter, SiteRequirement, Portfolio, WhyChooseUsSection, CaseStudySection

class CounterInline(admin.StackedInline):
	model = Counter
	extra = 0

class HeroSlideAdmin(admin.ModelAdmin):
	list_display = ['title', 'tagline']

class NumberCounterAdmin(admin.ModelAdmin):
	list_display = ['title', 'site']
	inlines = [CounterInline, ]

class CounterAdmin(admin.ModelAdmin):
	list_display = ['section', 'label']

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['heading', 'tagline', 'site']

class SiteRequirementAdmin(admin.ModelAdmin):
	list_display = ['title', 'location', 'helpline_number', 'helpline_email', 'site']

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['title', 'tagline', 'site']

class CaseStudySectionAdmin(admin.ModelAdmin):
	list_display = ['title', 'tagline', 'site']

class WhyChooseUsSectionAdmin(admin.ModelAdmin):
	list_display = ['section_title', 'site']

admin.site.register(HeroSlide, HeroSlideAdmin)
admin.site.register(NumberCounter, NumberCounterAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(SiteRequirement, SiteRequirementAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(CaseStudySection, CaseStudySectionAdmin)
admin.site.register(WhyChooseUsSection, WhyChooseUsSectionAdmin)
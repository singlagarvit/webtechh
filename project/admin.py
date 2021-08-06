from django.contrib import admin
from .models import Project, ProjectImage, CaseStudy, CaseStudySection, CaseStudyScoreBoard

class ProjectImageInline(admin.StackedInline):
	model = ProjectImage
	extra = 0

class CaseStudySectionInline(admin.StackedInline):
	model = CaseStudySection
	extra = 0

class CaseStudyScoreBoardInline(admin.StackedInline):
	model = CaseStudyScoreBoard
	extra = 0

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'service', 'website_link', 'featured']
	inlines = [ProjectImageInline, ]

class ProjectImageAdmin(admin.ModelAdmin):
	list_display = ['project', 'alt_tag']

class CaseStudyAdmin(admin.ModelAdmin):
	list_display = ['title', 'project', 'service', 'slug', 'featured']
	inlines = [CaseStudySectionInline, CaseStudyScoreBoardInline, ]

class CaseStudySectionAdmin(admin.ModelAdmin):
	list_display = ['title', 'case']

class CaseStudyScoreBoardAdmin(admin.ModelAdmin):
	list_display = ['pointer', 'case']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(CaseStudySection, CaseStudySectionAdmin)
admin.site.register(CaseStudyScoreBoard, CaseStudyScoreBoardAdmin)
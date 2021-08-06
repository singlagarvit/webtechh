from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from service.models import Service
from marketing.models import SEOTag

class Project(models.Model):
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=100, unique=True)
	thumbnail = models.ImageField(upload_to='project/thumbnails/')
	thumbnail_alt_tag = models.CharField(max_length=50, null=True, blank=True)
	description = RichTextField()
	website_link = models.URLField()
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class ProjectImage(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='project/images/')
	alt_tag = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return f'{self.project.title} - {self.id}'

class CaseStudy(models.Model):
	project = models.OneToOneField(Project, on_delete=models.SET_NULL, null=True, blank=True)
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
	tagline = models.CharField(max_length=100, null=True)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, editable=False)
	banner = models.ImageField(upload_to='project/banners/', null=True)
	alt_tag_banner = models.CharField(max_length=50, null=True, blank=True)
	description = RichTextField()
	featured = models.BooleanField(default=False)
	video_link = models.URLField(null=True, blank=True)
	featured_background = models.ImageField(upload_to='cases/featured/background/', null=True, blank=True)
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Case studies'
		ordering = ('-id', )

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(CaseStudy, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('project:case', kwargs={'case_slug': self.slug})

class CaseStudySection(models.Model):
	case = models.ForeignKey(CaseStudy, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='project/cases/images')
	alt_tag = models.CharField(max_length=50, null=True, blank=True)
	content = RichTextField()

	def __str__(self):
		return self.title

class CaseStudyScoreBoard(models.Model):
	case = models.ForeignKey(CaseStudy, on_delete=models.CASCADE)
	pointer = models.CharField(max_length=35)

	def __str__(self):
		return self.pointer
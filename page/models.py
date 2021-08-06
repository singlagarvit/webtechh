from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from marketing.models import SEOTag

class FooterPage(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, editable=False)
	content = RichTextUploadingField()
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(FooterPage, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('page:page', kwargs={'page_slug': self.slug})

class StaticPage(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	banner = models.ImageField(upload_to='pages/static/banners/')
	tagline = models.CharField(max_length=80, null=True, blank=True)
	button = models.CharField(max_length=20, null=True, blank=True)
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('page:page', kwargs={'page_slug': self.slug})

	def __str__(self):
		return self.title

class PageSection(models.Model):
	page = models.ForeignKey(StaticPage, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='pages/static/images/')
	alt_tag_image = models.CharField(max_length=50, null=True, blank=True)
	content = RichTextField()

	def __str__(self):
		return self.title
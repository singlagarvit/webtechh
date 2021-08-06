from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from marketing.models import SEOTag

class Service(models.Model):
	title = models.CharField(max_length=60, unique=True)
	common_name = models.CharField(max_length=20, null=True)
	slug = models.SlugField(max_length=60, editable=False, unique=True)
	icon = models.CharField(max_length=30, help_text=mark_safe("Please visit <a target='_blank' href='https://linearicons.com/free'>Linear Icons</a>"))
	lead_h1 = models.CharField(max_length=100, null=True, blank=True)
	service_tagline = models.CharField(max_length=100, null=True, blank=True)
	banner = models.ImageField(upload_to='services/banners/')
	content = RichTextField()
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('service:service', kwargs={'service_slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Service, self).save(*args, **kwargs)

class ServiceProcess(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	icon = models.CharField(max_length=30, help_text=mark_safe("Please visit <a target='_blank' href='https://linearicons.com/free'>Linear Icons</a>"))
	content = RichTextField()
	image = models.ImageField(upload_to='services/processes/')
	alt_tag_image = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Service processes'
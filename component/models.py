from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
from marketing.models import SEOTag

class HeroSlide(models.Model):
	title = models.CharField(max_length=50)
	tagline = models.CharField(max_length=60)
	banner = models.ImageField(upload_to='slides/banners/')

	def __str__(self):
		return self.title

class NumberCounter(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=100)
	background = models.ImageField(upload_to='component/counter/background/')

	def __str__(self):
		return self.title

class Counter(models.Model):
	section = models.ForeignKey(NumberCounter, on_delete=models.CASCADE)
	count = models.IntegerField()
	label = models.CharField(max_length=30)
	icon = models.CharField(max_length=30, help_text=mark_safe("Please visit <a target='_blank' href='https://linearicons.com/free'>Linear Icons</a>"))

	def __str__(self):
		return self.label

class Newsletter(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	heading = models.CharField(max_length=70)
	tagline = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.heading

class SiteRequirement(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='logo/')
	location = models.CharField(max_length=100)
	location_iframe = models.URLField(max_length=350)
	description = models.CharField(max_length=120)
	facebook = models.URLField(null=True,blank=True)
	twitter = models.URLField(null=True,blank=True)
	google_plus = models.URLField(null=True,blank=True)
	instagram = models.URLField(null=True,blank=True)
	pinterest = models.URLField(null=True,blank=True)
	linkedin = models.URLField(null=True,blank=True)
	helpline_number = models.CharField(max_length=10)
	helpline_email = models.EmailField()

	def __str__(self):
		return self.title

class Portfolio(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=50)
	tagline = models.CharField(max_length=120, null=True, blank=True)
	background = models.ImageField(upload_to='component/portfolio/background/')
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

class WhyChooseUsSection(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	section_title = models.CharField(max_length=50)
	content = RichTextField()

	def __str__(self):
		return self.section_title

class CaseStudySection(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=50)
	tagline = models.CharField(max_length=120, null=True, blank=True)
	background = models.ImageField(upload_to='component/case-studies/background/')
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Case studies'

class Contact(models.Model):
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=50)
	tagline = models.CharField(max_length=120, null=True, blank=True)
	background = models.ImageField(upload_to='component/contact/background/')
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title
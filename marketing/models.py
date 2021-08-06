from django.db import models

class SEOTag(models.Model):
	title = models.CharField(max_length=100, unique=True)
	desc = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title
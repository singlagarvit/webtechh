from django.db import models

class Query(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	website = models.CharField(max_length=50, null=True, blank=True)
	message = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Queries'
		ordering = ('-created_on', )

class Subscription(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-created_on', )
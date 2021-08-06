from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from marketing.models import SEOTag

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, editable=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:category', kwargs={'category_slug': self.slug})

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ('-id', )

class Tag(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, editable=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Tag, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:tag', kwargs={'tag_slug': self.slug})

	class Meta:
		ordering = ('-id', )

class Author(models.Model):
	name = models.CharField(max_length=100, unique=True)
	user_image = models.ImageField(upload_to='post/author/profile/')
	description = models.TextField()
	social_media_platform = models.CharField(max_length=50, null=True, blank=True)
	social_media_link = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, editable=False)
	banner = models.ImageField(upload_to='post/banners/')
	alt_tag_banner = models.CharField(max_length=100, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	content = RichTextUploadingField()
	tags = models.ManyToManyField(Tag)
	seo_tag = models.OneToOneField(SEOTag, on_delete=models.SET_NULL, null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:post', kwargs={'post_slug': self.slug})

	class Meta:
		ordering = ('-created_on', )

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	website = models.URLField(null=True, blank=True)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-timestamp', )

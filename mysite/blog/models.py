import random

from django.db import models

# Create your models here.

class PostEntryQuery(models.QuerySet):
	def published(self):
		return self.filter(published=True)

	def randomPost(self):
		return self.published().order_by('?')[:4]

	def getFeaturedPost(self):
		return random.choice(self.published())
	

class PostTag(models.Model):
	tag = models.CharField(max_length=30)

	def __str__(self):
		return self.tag


class PostEntry(models.Model):
	title = models.CharField(max_length=200)
	hero_image = models.ImageField(upload_to='blog/media/')
	post_body = models.TextField()
	post_image = models.ImageField(upload_to='blog/media/', blank=True)
	author = models.CharField(max_length=30)
	created = models.DateTimeField('date published')
	slug = models.SlugField(max_length=200, unique=True)
	published = models.BooleanField(default=True)

	tags = models.ManyToManyField(PostTag)
	objects = PostEntryQuery.as_manager()

	def __str__(self):
		return self.title

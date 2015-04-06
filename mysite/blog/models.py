from django.db import models

# Create your models here.

class PostEntryQuery(models.QuerySet):
	def published(self):
		return self.filter(published=True)


class PostEntry(models.Model):
	title = models.CharField(max_length=200)
	hero_image = models.ImageField(upload_to='med/blogphotos/%Y/%m/%d')
	post_body = models.TextField()
	post_image = models.ImageField(upload_to='media/blogphotos/%Y/%m/%d', blank=True)
	author = models.CharField(max_length=30)
	created = models.DateTimeField('date published')
	slug = models.SlugField(max_length=200, unique=True)
	published = models.BooleanField(default=True)

	objects = PostEntryQuery.as_manager()

	def __str__(self):
		return self.title

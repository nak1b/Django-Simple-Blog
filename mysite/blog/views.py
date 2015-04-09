import random
from django.http import Http404
from django.shortcuts import render
from . import models

def Index(request):
	posts = models.PostEntry.objects.published().order_by('-created')
	randomPosts = models.PostEntry.objects.randomPost()
	featuredPost = models.PostEntry.objects.getFeaturedPost()
	context = {'posts': posts, 'randomPosts': randomPosts, 'featuredPost': featuredPost}
	return  render(request, 'blog/index.html', context)
	
def Article(request, article_slug):
	article = models.PostEntry.objects.get(slug=article_slug)
	randomPosts = models.PostEntry.objects.randomPost() 
	context = {'article' : article,  'randomPosts': randomPosts}
	return render(request, 'blog/article.html', context)

# Create your views here.

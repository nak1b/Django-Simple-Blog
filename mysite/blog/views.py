from django.http import Http404
from django.shortcuts import render
from . import models

def Index(request):
	posts = models.PostEntry.objects.published().order_by('-created')
	context = {'posts': posts}
	return  render(request, 'blog/index.html', context)
	
def Article(request, article_slug):
	article = models.PostEntry.objects.get(slug=article_slug)
	context = {'article' : article}
	return render(request, 'blog/article.html', context)

# Create your views here.

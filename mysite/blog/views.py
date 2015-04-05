from django.http import Http404
from django.shortcuts import render
from . import models

def Index(request):
	posts = models.PostEntry.objects.published().order_by('-created')
	context = {'posts': posts}
	return  render(request, 'blog/index.html', context)
	

# Create your views here.

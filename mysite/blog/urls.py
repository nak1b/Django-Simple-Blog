from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Index, name="index"),
    url(r'^(?P<article_id>[0-9]+)/$', views.Article, name="article"),
  
]

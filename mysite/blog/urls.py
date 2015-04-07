from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Index, name="index"),
    url(r'^(?P<article_slug>[\w\-]+)/$', views.Article, name="article"),
    
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

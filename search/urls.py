from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'search.views.router'),
    url(r'^intern$', 'search.views.intern'),
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('resume.views',
    url(r'^add/$', 'ReferencePosting'),
    url(r'update/$', 'update'),
    url(r'(?P<reference_id>\d+)/edit/$', 'edit'),
    url(r'(?P<reference_id>\d+)/delete/$', 'delete'),
)

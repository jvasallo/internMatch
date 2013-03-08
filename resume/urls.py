from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('resume.views',
    url(r'^add/$', 'ReferencePosting'),
    url(r'^edit/$', 'edit'),
)

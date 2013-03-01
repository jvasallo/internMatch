from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('resume.views',
    url(r'^$', 'ResumePosting'),
    url(r'^edit/$', 'edit'),
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'resume.views.ResumePosting'),
    url(r'^edit/$', 'resume.views.editResume'),
)

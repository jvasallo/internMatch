from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('resume.views',
    url(r'^add/$', 'ResumePosting'),
    url(r'^edit/$', 'edit'),
    url(r'(?P<resume_post_id>\d+)/$', 'detail'),
)

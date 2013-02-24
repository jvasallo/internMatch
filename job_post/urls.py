from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'job_post.views.JobPosting'),
    url(r'(?P<job_post_id>\d+)/$', 'job_post.views.detail'),
)

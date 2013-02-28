from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('job_post.views',
    url(r'^$', 'JobPosting'),
    url(r'(?P<job_post_id>\d+)/$', 'detail'),
    url(r'(?P<job_post_id>\d+)/delete/$', 'deletePost'),
)

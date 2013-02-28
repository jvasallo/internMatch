from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('quiz.views',
    url(r'^$', 'index'),
    url(r'^quiz/$', 'quiz'),
    url(r'^submit/$', 'submit'),
    url(r'^complete/$', 'complete'),
)

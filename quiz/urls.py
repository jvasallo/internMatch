from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'quiz.views.index'),
    url(r'quiz/$', 'quiz.views.quiz'),
    url(r'submit/$', 'quiz.views.submit'),
    url(r'complete/$', 'quiz.views.complete'),
)

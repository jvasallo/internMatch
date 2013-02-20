from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'quiz.views.index'),
    url(r'begin/$', TemplateView.as_view(template_name="quiz/begin.html")),
    url(r'submit/$', 'quiz.views.submit'),
    url(r'complete/$', TemplateView.as_view(template_name="quiz/complete.html")),
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^send$', TemplateView.as_view(template_name="signin.html")),
    #url(r'^send$', 'quiz.views.QuizResultsParsing'),
)
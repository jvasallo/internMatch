from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^r$', 'register.views.InternRegistration'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^1$', TemplateView.as_view(template_name="complete.html")),
    url(r'^3$', TemplateView.as_view(template_name="quiz.html")),
    url(r'^4$', TemplateView.as_view(template_name="signin.html")),
    url(r'^5$', TemplateView.as_view(template_name="company.html")),
)
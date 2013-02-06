from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^r$', 'register.views.InternRegistration'),
    url(r'^intern$', TemplateView.as_view(template_name="intern.html")),
    url(r'^company$', TemplateView.as_view(template_name="company.html")),
    url(r'^complete$', TemplateView.as_view(template_name="complete.html")),
    url(r'^quiz$', TemplateView.as_view(template_name="quiz.html")),
)
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^intern$', 'register.views.InternRegistration'),
    #url(r'^intern$', TemplateView.as_view(template_name="intern.html")),
    url(r'^company$', 'register.views.CompanyRegistration'),
    url(r'^login$', 'register.views.Signin'),
    url(r'^quiz/submit', 'register.views.QuizResultsParsing'),
    url(r'^complete$', TemplateView.as_view(template_name="complete.html")),
    url(r'^quiz$', TemplateView.as_view(template_name="quiz.html")),
    url(r'^signin$', TemplateView.as_view(template_name="signin.html")),
)
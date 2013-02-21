from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^intern$', 'register.views.InternRegistration'),
    url(r'^company$', 'register.views.CompanyRegistration'),
)

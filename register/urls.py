from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('register.views',
    url(r'^intern$', 'InternRegistration'),
    url(r'^company$', 'CompanyRegistration'),
)

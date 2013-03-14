from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
    url(r'^about/', 'home.views.about'),
    url(r'^contact/', 'home.views.contact'),
    url(r'^legal/', 'home.views.legal'),
    url(r'^login$', 'home.views.Login'),
    url(r'^logout$', 'home.views.Logout'),                   
    url(r'^register/', include('register.urls')),
    url(r'^profile/', include('account.urls')),
    url(r'^job-post/', include('job_post.urls')),
    url(r'^references/', include('resume.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^search/', include('search.urls')),
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('account.views',
    url(r'^$', 'index'),
    url(r'^settings/$', 'settings'),
    url(r'deactivate/$', 'deactivate'),
    url(r'edit/$', 'edit'),
    url(r'update/$', 'update'),
    url(r'companies/$', 'companies'),
    url(r'jobs/$', 'jobs'),
    url(r'company/(?P<company_id>\d+)/$', 'publicCompanyProfile'),
    url(r'intern/(?P<intern_id>\d+)/$', 'privateInternProfile'),
)

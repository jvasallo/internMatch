from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'account.views.index'),
    url(r'add/$', 'account.views.add'),
    url(r'edit/$', 'account.views.edit'),
    url(r'company/(?P<company_id>\d+)/$', 'account.views.publicCompanyProfile'),
    url(r'intern/(?P<intern_id>\d+)/$', 'account.views.privateInternProfile'),
)

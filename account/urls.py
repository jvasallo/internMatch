from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^profile/$', 'account.views.view_profile'),
    url(r'intern/$', 'account.views.sample_intern'),
    url(r'company/$', 'account.views.sample_company'),
    url(r'company/addjob/$', TemplateView.as_view(template_name="account/addjob.html")),
)

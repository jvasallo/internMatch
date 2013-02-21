from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
    url(r'^about/', 'home.views.about'),
    url(r'^contact/', 'home.views.contact'),
    url(r'^login$', 'home.views.Login'),
    url(r'^logout$', 'home.views.Logout'),
    url(r'^register/', include('register.urls')),
    url(r'^profile/', include('account.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^search/', TemplateView.as_view(template_name="search/search.html")),
    url(r'^search_co/', TemplateView.as_view(template_name="search/co_search.html")),
)

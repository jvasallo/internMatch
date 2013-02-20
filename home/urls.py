from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    url(r'^search/', TemplateView.as_view(template_name="search/search.html")),
    url(r'^search_co/', TemplateView.as_view(template_name="search/co_search.html")),
    url(r'^register/', include('register.urls')),
    url(r'^profile/', include('account.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^login$', 'home.views.Login'),
    url(r'^logout$', 'home.views.Logout'),
)

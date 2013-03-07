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
    url(r'^forgot$', 'home.views.Forgot'),
    url(r'^logout$', 'home.views.Logout'),                   
    url(r'^register/', include('register.urls')),
    url(r'^profile/', include('account.urls')),
    url(r'^job-post/', include('job_post.urls')),
    url(r'^references/', include('resume.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^search/', include('search.urls')),
##    url(r'^user/password/reset/$', 
##        'django.contrib.auth.views.password_reset', 
##        {'post_reset_redirect' : '/user/password/reset/done/'},
##        name="password_reset"),
##    (r'^user/password/reset/done/$',
##        'django.contrib.auth.views.password_reset_done'),
##    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
##        'django.contrib.auth.views.password_reset_confirm', 
##        {'post_reset_redirect' : '/user/password/done/'}),
##    (r'^user/password/done/$', 
##        'django.contrib.auth.views.password_reset_complete')),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)

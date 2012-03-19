from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stripetest.views.home', name='home'),
    # url(r'^stripetest/', include('stripetest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^charge/', 'sales.views.charge', name='charge'),
    url(r'^create/', 'sales.views.create', name='create'),
    url(r'^subscribe/', 'sales.views.subscribe', name='subscribe'),
    url(r'^admin/', include(admin.site.urls)),
)

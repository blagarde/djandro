from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djandro.views.home', name='home'),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

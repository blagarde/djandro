from django.conf.urls import patterns, include, url
from views import log
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djandro.views.home', name='home'),
    url(r'^logging/', log),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

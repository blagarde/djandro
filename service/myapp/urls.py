from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^', 'myapp.views.hello'),
)

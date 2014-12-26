from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
                       # blog views
                       url(r'^$', index),
                       url(r'^blog/(?P<post_id>\d+)$', post),
                       url(r'^blog/create/$', post_new),
                       # admin views
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import post_new

urlpatterns = patterns('',
                       # blog views
                       url(r'^blog/create/$', post_new),
                       # admin views
                       url(r'^admin/', include(admin.site.urls)),
                       )

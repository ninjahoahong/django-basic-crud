from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index, post, post_edit, post_new, post_delete
from blog.rest_views import PostList, PostDetail


urlpatterns = patterns('',
                       # blog views
                       url(r'^$', index),
                       url(r'^blog/(?P<post_id>\d+)$', post),
                       url(r'^blog/edit/(?P<post_id>\d+)$', post_edit),
                       url(r'^blog/delete/(?P<post_id>\d+)$', post_delete),
                       url(r'^blog/create/$', post_new),

                       # RESTful API
                       url(r'^api/blog/$', PostList.as_view(),
                           name="post-list"),
                       url(r'^api/blog/(?P<pk>\d+)$',
                           PostDetail.as_view(), name="post-detail"),

                       # admin views
                       url(r'^admin/', include(admin.site.urls)),
                       )

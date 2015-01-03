from django.conf.urls import patterns, url
from blog.views import post, post_edit, post_new, post_delete
from api.views import PostList, PostDetail


urlpatterns = patterns("",
                       url(r"^blog/$", PostList.as_view(),
                           name="post-list"),
                       url(r"^blog/(?P<pk>\d+)$",
                           PostDetail.as_view(), name="post-detail"),
                       )

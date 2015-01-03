from django.conf.urls import patterns, url
from blog.views import post, post_edit, post_new, post_delete


urlpatterns = patterns("",
                       url(r"^(?P<post_id>\d+)$", post),
                       url(r"^edit/(?P<post_id>\d+)$", post_edit),
                       url(r"^delete/(?P<post_id>\d+)$", post_delete),
                       url(r"^create/$", post_new),
                       )

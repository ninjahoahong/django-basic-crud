from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index


urlpatterns = patterns("",
                       # blog views
                       url(r"^$", index, name="index"),
                       url(r"^blog/", include("blog.urls")),

                       # RESTful API
                       url(r"^api/", include("api.urls")),

                       # admin views
                       url(r"^admin/", include(admin.site.urls)),
                       )

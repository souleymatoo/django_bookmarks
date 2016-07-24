from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import *
import os
site_media = os.path.join(
        os.path.dirname(__file__), 'static'
)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$|^dashboard$', main_page2),
    url(r'^user/(\w+)/$', user_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),
]

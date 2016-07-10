from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'^dashboard$', main_page1),
]

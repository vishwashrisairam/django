from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'reg.views.home', name='home'),
    url(r'^register', 'reg.views.register', name='register'),
    url(r'^login', 'reg.views.user_login', name='login'),
    url(r'^logout', 'reg.views.user_logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)

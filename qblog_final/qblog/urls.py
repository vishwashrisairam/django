from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('blog.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    url(r'^admin/', include(admin.site.urls)),

)

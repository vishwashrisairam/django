from django.conf.urls import patterns,include,url
from . import views,feed

urlpatterns=patterns('',
	url(r'^$',views.BlogIndex.as_view(),name="index"),
	url(r'^new/',views.new,name="new"),
	url(r'^feed/$',feed.LatestPosts(),name="feed"),
	url(r'^(?P<slug>[-\w]+)/$', views.single_post, name='single'),
	url(r'^entry/(?P<slug>\S+)$',views.BlogIndex.as_view(),name="entry_detail"),
) 
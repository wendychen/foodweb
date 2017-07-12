from django.conf.urls import url
# from django.contrib import admin

#from django.contrib.auth import views
from . import views

urlpatterns = [

  # What does 'r' doing here?
  # My imagine is r is the reference of path

  # There is the calling of method, why is there also variable of name?

	url(r'^$', views.post_list, name='post_list'),
  url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
  url(r'^addpost$', views.add_post, name='add_post'),
  url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
  url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
  url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
  url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
  url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'), 
  url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
  url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
 ]

from django.conf.urls import url
from django.contrib import admin

#from . import views
from posts.views import post_list, post_create, post_detail, post_update, post_delete
#from posts.views import post_create
#from posts.views import post_detail
#from posts.views import post_update
#from posts.views import post_delete

urlpatterns = [
    url(r'^$', post_list, name='list'),  #url(r'^$', posts.views.post_list) i am not able to do using this way. gettin callable error.
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name = 'detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]
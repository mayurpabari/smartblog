from django.conf.urls import url
from .import views
#from polls.views import index,detail,results,vote

app_name = 'polls'

urlpatterns = [

	url(r'^$', views.IndexView.as_view(), name='index'), #why we write name here ?
	url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
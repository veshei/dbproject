from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.calendar_list, name = 'calendar_list'),
	url(r'^orgcalendar/(?P<pk>\d+)/$', views.org_calendar_list, name='org_calendar_list'),
	url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'), 
	url(r'^event/new/$', views.event_new, name='event_new'), 
	url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'), 
	url(r'^event/(?P<pk>\d+)/remove/$', views.event_remove, name='event_remove'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
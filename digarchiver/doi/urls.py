from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^process$', views.process, name="process"),
	url(r'^details/(?P<project_id>[0-9]+)$', views.details, name='details'),
	url(r'^processdetails$', views.processdetails, name="processdetails"),
	url(r'^share$', views.share, name="share"),
]
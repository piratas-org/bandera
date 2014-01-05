from django.conf.urls import patterns, include, url

from meme import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/bandera/supporter', views.supporter, name='supporter'),
	url(r'^api/bandera/candidate', views.candidate, name='candidate'),
	url(r'^thanks$', views.thanks, name='thanks'),
	url(r'^manifesto$', views.manifesto, name='manifesto'),
	url(r'^privacy$', views.privacy, name='privacy'),
	url(r'^tos$', views.tos, name='tos'),
)
handler403 = 'meme.views.custom_403'
handler404 = 'meme.views.custom_404'
handler500 = 'meme.views.custom_500'

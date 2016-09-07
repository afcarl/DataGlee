from django.conf.urls import include,url
from . import views

urlpatterns = [
url(r'^$', views.homepage, name= 'homepage'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
url(r'^yelping$', views.yelping, name='yelping'),
url(r'^IndianRailways$', views.IndianRailways, name='IndianRailways'),
url(r'^Gapminder$', views.Gapminder, name='Gapminder'),
url(r'^Youtube$', views.Youtube, name='Youtube'),

# url(r'^trial$', views.trial, name='trial'),

]
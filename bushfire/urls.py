from django.conf.urls import patterns, include, url
from bushfire.models import Bushfire
from bushfire import views

urlpatterns = patterns('',
    url(r'^$', views.BushfireView.as_view(), name='index'),
    #url(r'(?P<pk>\d+)/$', views.BushfireDetailView.as_view(), name='bushfire_detail'),
    #url(r'(?P<pk>\d+)/$', views.BushfireCreateView.as_view(), name='bushfire_detail'),
    #url(r'(?P<pk>\d+)/$', views.BushfireUpdateView.as_view(), name='bushfire_update'),
    url(r'(?P<pk>\d+)/$', views.BushfireUpdateView.as_view(), name='bushfire_form'),

)


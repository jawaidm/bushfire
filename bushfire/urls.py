from django.conf.urls import patterns, include, url
from bushfire.models import Bushfire
from bushfire import views

urlpatterns = patterns('',
    url(r'^$', views.BushfireView.as_view(), name='index'),
    url(r'create/$', views.BushfireCreateView.as_view(), name='bushfire_create'),
    url(r'create2/$', views.BushfireCreateTest2View.as_view(), name='bushfire_create2'),
    url(r'create_test/$', views.BushfireCreateTestView.as_view(), name='bushfire_create_test'),
#    url(r'^$', views.BushfireView.as_view(), name='index'),
    url(r'(?P<pk>\d+)/$', views.BushfireUpdateView.as_view(), name='bushfire_form'),

    #url(r'(?P<pk>\d+)/$', views.BushfireDetailView.as_view(), name='bushfire_detail'),
    #url(r'(?P<pk>\d+)/$', views.BushfireCreateView.as_view(), name='bushfire_detail'),
    #url(r'(?P<pk>\d+)/$', views.BushfireUpdateView.as_view(), name='bushfire_update'),

)


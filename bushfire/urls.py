from django.conf.urls import patterns, include, url
from bushfire.models import Bushfire
from bushfire import views

urlpatterns = patterns('',
    url(r'^$', views.BushfireView.as_view(), name='index'),
    url(r'(?P<pk>\d+)/$', views.BushfireDetailView.as_view(), name='bushfire_detail'),
    #url(r'bushfire/$', views.BushfireView.as_view(), name='bushfire'),
    #url(r'permutations/(?P<pk>\d+)/$', views.PermutationView.as_view(), name='permutations'),

)

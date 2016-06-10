from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bushfire_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login',
        kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',
        kwargs={'template_name': 'logged_out.html'}),

#    url(r'^$', TemplateView.as_view(template_name="home.html")),


    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^bushfire/', include('bushfire.urls', namespace='bushfire')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from main.views.public import register, index
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('main.views.public',
  (r'^$', 'index'),
  ('^register/$', register),
  (r'^accounts/login/$',  login),
  (r'^accounts/logout/$', logout),
)

urlpatterns += patterns('',
  url(r'^admin/', include(admin.site.urls)),
  (r'^public/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT }),
)

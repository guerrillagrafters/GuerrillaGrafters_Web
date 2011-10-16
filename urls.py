from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views.public',
  (r'^$', 'index'),
)

urlpatterns += patterns('',
  url(r'^admin/', include(admin.site.urls)),
  (r'^public/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT }),
)

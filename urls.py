from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from main.views.public import register, index
from django.contrib import admin
from main.forms import *
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('main.views.public',
  (r'^$', 'index'),
  ('^register/$', register),
  (r'^accounts/login/$',  login, {'authentication_form' : CustomAuthenticationForm}),
  (r'^accounts/logout/$', logout),
  (r'^accounts/profile/$', lambda x: HttpResponseRedirect('/')), # temporary
  
)

urlpatterns += patterns('main.views.tree',
  (r'^add_tree/$', 'add_tree'),
)

urlpatterns += patterns('',
  url(r'^admin/', include(admin.site.urls)),
  (r'^public/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT }),
)

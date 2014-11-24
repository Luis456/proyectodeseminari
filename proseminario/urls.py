from django.conf.urls import patterns, include, url
from django.contrib import admin
from proseminario.apps.usuarios.views import *
from proseminario.apps.principal.views import *
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proseminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^blog/', include("proseminario.apps.usuarios.urls")),
    url(r'^blog/', include("proseminario.apps.principal.url")),
   
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)

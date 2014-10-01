from django.conf.urls import patterns, include, url
from django.contrib import admin
from proseminario.apps.usuarios.views import pagina_principal

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proseminario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', pagina_principal),
)

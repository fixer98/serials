from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from ser.models import Post

admin.autodiscover()

urlpatterns = patterns('',
    url(r'serials/', 'ser.views.index'),
    url(r'^ulogin/', include('django_ulogin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
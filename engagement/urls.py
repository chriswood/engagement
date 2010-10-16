from django.conf.urls.defaults import *
from views import engagement
from django.conf import settings

urlpatterns = patterns('',
    # (r'^engagement/', include('engagement.foo.urls')),
    url(r'engagement/$', engagement), 
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DOC_ROOT}),
)

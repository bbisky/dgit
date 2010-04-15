from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',  
)
# url for static
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_PATH}),                    
                            )

#urls for wap
urlpatterns += patterns('',                        
                        (r'^djangogit/', include('apps.djangogit.urls')),
                        )
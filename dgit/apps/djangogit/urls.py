from django.conf.urls.defaults import *

urlpatterns = patterns('apps.djangogit.views',
                       url(r'^$', 'index', name='index'),  
                        )
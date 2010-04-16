from django.conf.urls.defaults import *

urlpatterns = patterns('apps.djangogit.views',
                    url(r'^$', 'index', name='index'),
#                    url(r'^(?P<repo_path>.*?)/tree/(?P<sha>.*?)/blob/(?P<blob_path>.*?)$', 'viewblob', name='viewblob'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/tree/(?P<sha>([\w\d]+)?)/(?P<from_path>.*?)$', 'tree', name='tree'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/tree/(?P<sha>([\w\d]+)?)/$', 'tree', name='tree'),
                    url(r'^(?P<repo_path>.*?)/commit/(?P<sha>.*)/$', 'commit', name='commit'),
                    url(r'^(?P<repo_path>.*?)/$', 'repository', name='repository'),
)
from django.conf.urls.defaults import *

urlpatterns = patterns('apps.djangogit.views',
                    url(r'^$', 'index', name='index'),
#                    url(r'^(?P<repo_path>.*?)/tree/(?P<sha>.*?)/blob/(?P<blob_path>.*?)$', 'viewblob', name='viewblob'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/tree/(?P<sha>([\w\d]+)?)/(?P<from_path>.*?)$', 'tree_view', name='tree'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/tree/(?P<sha>([\w\d]+)?)$', 'tree_view', name='tree'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/blob/(?P<sha>([\w\d]+)?)/(?P<from_path>.*?)$', 'blob_view', name='blob'),
                    url(r'^(?P<repo_path>([\w_/\.]+)?)/raw/(?P<sha>([\w\d]+)?)/(?P<from_path>.*?)$', 'blob_raw', name='blob_raw'),
                    url(r'^(?P<repo_path>.*?)/commit/(?P<sha>([\w\d]+)?)$', 'commit_view', name='commit'),
                    url(r'^(?P<repo_path>.*?)/commit/(?P<sha>([\w\d]+)?)/diff$', 'commit_diff', name='commit_diff'),
                    url(r'^(?P<repo_path>.*?)$', 'repository', name='repository'),
)
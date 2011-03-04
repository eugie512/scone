from django.conf.urls.defaults import *

urlpatterns = patterns('listings.views',
    (r'^$', 'index'),
    (r'^(?P<list_id>\d+)/$', 'details'),
)

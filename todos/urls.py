from django.conf.urls import url, include
from .views import index, details, add

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', details),
    url(r'^add/$', add, name='add'),
]
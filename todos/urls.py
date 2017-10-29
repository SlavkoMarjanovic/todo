from django.conf.urls import url, include
from .views import index, details, add, TodoList

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', details),
    url(r'^add/$', add, name='add'),
    url(r'^api/$', TodoList.as_view()),
]
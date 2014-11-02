from django.conf.urls import patterns, include, url
from app.views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, listar

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TodoList.as_view(), name='app_list'),
    url(r'^Todo(?P<pk>\d+)$', TodoDetail.as_view(), name='app_detail'),
    url(r'^New$', TodoCreate.as_view(), name='app_create'),
    url(r'^Todo(?P<pk>\d+)/Update$', TodoUpdate.as_view(), name='app_update'),
    url(r'^Todo(?P<pk>\d+)/Delete$', TodoDelete.as_view(), name='app_delete'),
    url(r'^listar/todo$', 'app.views.listar'),
    url(r'^admin/', include(admin.site.urls)),
)

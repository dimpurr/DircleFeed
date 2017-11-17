from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<list_name>[\w-]+)$', views.list_view, name='list_view'),
]
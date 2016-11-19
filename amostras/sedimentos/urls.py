from django.conf.urls import url
from .import views


app_name='sedimentos'

urlpatterns=[
    #se refere a /resident/
    url(r'^$',views.index,name='index'),
    # se refere a uma em especifico/
    url(r'^(?P<amostra_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<amostra_id>[0-9]+)/destaque$', views.destaque, name='destaque'),


]
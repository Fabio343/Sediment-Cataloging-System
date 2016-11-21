from django.conf.urls import url
from .import views


app_name='sedimentos'

urlpatterns=[
    #se refere a /resident/
    url(r'^$',views.IndexView.as_view(),name='index'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),



]

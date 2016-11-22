from django.conf.urls import url
from . import views

app_name = 'sedimentos'

urlpatterns = [
    # se refere a /resident/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'amostra/add/$', views.amostraCreate.as_view(), name='amostra-add'),
    url(r'amostra/(?P<pk>[0-9]+)/$', views.amostraUpdate.as_view(), name='amostra-Update'),
    url(r'amostra/(?P<pk>[0-9]+)/$', views.amostraDelete.as_view(), name='amostra-Delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]


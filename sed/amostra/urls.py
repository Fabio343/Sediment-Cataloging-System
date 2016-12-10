from django.conf.urls import url
from . import views

app_name = 'amostra'

urlpatterns = [
    # se refere a /resident/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'amostra/add/$', views.amostraCreate.as_view(), name='amostra-add'),
    url(r'amostra/(?P<pk>[0-9]+)/$', views.amostraUpdate.as_view(), name='amostra-Update'),
    url(r'amostra/(?P<pk>[0-9]+)/$', views.amostraDelete.as_view(), name='amostra-Delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),




    url(r'^$', views.IndexView2.as_view(), name='index2'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView2.as_view(), name='detail2'),
    url(r'continente/add/$', views.continenteCreate.as_view(), name='continente-add'),
    url(r'continente/(?P<pk>[0-9]+)/$', views.continenteUpdate.as_view(), name='continente-Update'),
    url(r'continente/(?P<pk>[0-9]+)/$', views.continenteDelete.as_view(), name='continente-Delete'),




    url(r'^$', views.IndexView3.as_view(), name='index3'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView3.as_view(), name='detail5'),
    url(r'cidade/add/$', views.cidadeCreate.as_view(), name='cidade-add'),
    url(r'cidade/(?P<pk>[0-9]+)/$', views.cidadeUpdate.as_view(), name='cidade-Update'),
    url(r'cidade/(?P<pk>[0-9]+)/$', views.cidadeDelete.as_view(), name='cidade-Delete'),





    url(r'^$', views.IndexView4.as_view(), name='index4'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView4.as_view(), name='detail4'),
    url(r'estado/add/$', views.estadoCreate.as_view(), name='estado-add'),
    url(r'estado/(?P<pk>[0-9]+)/$', views.estadoUpdate.as_view(), name='estado-Update'),
    url(r'estado/(?P<pk>[0-9]+)/$', views.estadoDelete.as_view(), name='estado-Delete'),





    url(r'^$', views.IndexView5.as_view(), name='index5'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView5.as_view(), name='detail3'),
    url(r'país/add/$', views.paísCreate.as_view(), name='país-add'),
    url(r'país/(?P<pk>[0-9]+)/$', views.paísUpdate.as_view(), name='país-Update'),
    url(r'país/(?P<pk>[0-9]+)/$', views.paísDelete.as_view(), name='país-Delete'),





    url(r'^$', views.IndexView6.as_view(), name='index6'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView6.as_view(), name='detail6'),
    url(r'ambiente/add/$', views.ambienteCreate.as_view(), name='ambiente-add'),
    url(r'ambiente/(?P<pk>[0-9]+)/$', views.ambienteUpdate.as_view(), name='ambiente-Update'),
    url(r'ambiente/(?P<pk>[0-9]+)/$', views.ambienteDelete.as_view(), name='ambiente-Delete'),






    url(r'^$', views.IndexView7.as_view(), name='index7'),
    # se refere a uma em especifico/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView7.as_view(), name='detail7'),
    url(r'clima/add/$', views.climaCreate.as_view(), name='clima-add'),
    url(r'clima/(?P<pk>[0-9]+)/$', views.climaUpdate.as_view(), name='clima-Update'),
    url(r'clima/(?P<pk>[0-9]+)/$', views.climaDelete.as_view(), name='clima-Delete'),



    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),


]

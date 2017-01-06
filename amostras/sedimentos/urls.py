from django.conf.urls import url
from . import views

app_name = 'sedimentos'

urlpatterns = [

    # se refere a /resident/
    url(r'^$', views.index, name='index'),
    # se refere a uma em especifico/
    url(r'^(?P<amostra_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_amostra/$', views.create_amostra, name='create_amostra'),
    url(r'^(?P<amostra_id>[0-9]+)/delete_amostra/$', views.delete_amostra, name='delete_amostra'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^$', views.contid, name='contid'),
    # se refere a uma em especifico/
    url(r'^(?P<continente_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'continente/add/$', views.create_continente, name='create_continente'),
    url(r'continente/(?P<pk>[0-9]+)/$', views.delete_continente, name='delete_continente'),

    url(r'^$', views.index3, name='index3'),
    # se refere a uma em especifico/
    url(r'^(?P<cidade_id>[0-9]+)/$', views.detail5, name='detail'),
    url(r'cidade/add/$', views.create_cidade, name='create_cidade'),
    url(r'cidade/(?P<pk>[0-9]+)/$', views.delete_cidade, name='delete_cidade'),

    url(r'^$', views.index4, name='index4'),
    # se refere a uma em especifico/
    url(r'^(?P<estado_id>[0-9]+)/$', views.detail4, name='detail'),
    url(r'estado/add/$', views.create_estado, name='create_estado'),
    url(r'estado/(?P<pk>[0-9]+)/$', views.delete_estado, name='delete_estado'),

    url(r'^$', views.index5, name='index5'),
    # se refere a uma em especifico/
    url(r'^(?P<país_id>[0-9]+)/$', views.detail3, name='detail'),
    url(r'país/add/$', views.create_país, name='create_país'),
    url(r'país/(?P<pk>[0-9]+)/$', views.delete_país, name='delete_país'),

    url(r'^$', views.index6, name='index6'),
    # se refere a uma em especifico/
    url(r'^(?P<ambiente_id>[0-9]+)/$', views.detail6, name='detail'),
    url(r'ambiente/add/$', views.create_ambiente, name='create_ambiente'),
    url(r'ambiente/(?P<pk>[0-9]+)/$', views.delete_ambiente, name='delete_ambiente'),

     url(r'^$', views.index7, name='index7'),
    # se refere a uma em especifico/
    url(r'^(?P<clima_id>[0-9]+)/$', views.detail7, name='detail'),
    url(r'clima/add/$', views.create_clima, name='create_clima'),
    url(r'clima/(?P<pk>[0-9]+)/$', views.delete_clima, name='delete_clima'),

    # se refere a uma em especifico/
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^adicionar/$', views.adicionar, name='adicionar'),
    url(r'^register/$', views.register, name='register'),
    # filtros/
    url(r'^continentes/(?P<filter_by>[a-zA_Z]+)/$', views.continentes, name='continentes'),
    url(r'^estados/(?P<filter_by>[a-zA_Z]+)/$', views.estados, name='estados'),
    url(r'^cidades/(?P<filter_by>[a-zA_Z]+)/$', views.cidades, name='cidades'),
    url(r'^paíss/(?P<filter_by>[a-zA_Z]+)/$', views.paíss, name='paíss'),
    url(r'^climas/(?P<filter_by>[a-zA_Z]+)/$', views.climas, name='climas'),
    url(r'^ambientes/(?P<filter_by>[a-zA_Z]+)/$', views.ambientes, name='ambientes'),


]


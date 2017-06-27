# urls definidas para as visualizações do sistema cada bloco de url esta definindo quais são as funções de cada uma delas
from django.conf.urls import url
from django.contrib.auth.views import   password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django_filters.views import FilterView
from . filters import amostraFilter

app_name = 'catalogação'

urlpatterns = [
   # se refere a pagina inicial e contato com administração/
    url(r'^$', views.index, name='index'),
    url(r'^$', views.amostra, name='amostra'),
    url(r'^contato/$', views.contato),
    url(r'^inicial/$', views.inicial, name='inicial'),

   # se refere a vizualização de detalhes dos exemplares bem como criação de novas amostras e também sua exclusão cada mini bloco representa uma das informações presentes no sistema/
    url(r'^(?P<amostra_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_amostra/$', views.create_amostra, name='create_amostra'),
    url(r'^(?P<amostra_id>[0-9]+)/delete_amostra/$', views.delete_amostra, name='delete_amostra'),

    url(r'^(?P<continente_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'continente/add/$', views.create_continente, name='create_continente'),
    url(r'continente/(?P<continente_id>[0-9]+)/$', views.delete_continente, name='delete_continente'),

    url(r'^(?P<cidade_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'cidade/add/$', views.create_cidade, name='create_cidade'),
    url(r'cidade/(?P<cidade_id>[0-9]+)/$', views.delete_cidade, name='delete_cidade'),

    url(r'^(?P<estado_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'estado/add/$', views.create_estado, name='create_estado'),
    url(r'estado/(?P<estado_id>[0-9]+)/$', views.delete_estado, name='delete_estado'),

    url(r'^(?P<país_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'país/add/$', views.create_país, name='create_país'),
    url(r'país/(?P<país_id>[0-9]+)/$', views.delete_país, name='delete_país'),

    url(r'^(?P<ambiente_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'ambiente/add/$', views.create_ambiente, name='create_ambiente'),
    url(r'ambiente/(?P<ambiente_id>[0-9]+)/$', views.delete_ambiente, name='delete_ambiente'),

    url(r'^(?P<clima_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'clima/add/$', views.create_clima, name='create_clima'),
    url(r'clima/(?P<clima_id>[0-9]+)/$', views.delete_clima, name='delete_clima'),

    # se refere a login,cadastros,creditos e demais detalhes ao desenvolvimentos/
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^adicionar/$', views.adicionar, name='adicionar'),
    url(r'^agradecimentos/$', views.agradecimentos, name='agradecimentos'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # filtros usados na pesquisa simples/
    url(r'^continentes/(?P<filter_by>[a-zA_Z]+)/$', views.continentes, name='continentes'),
    url(r'^estados/(?P<filter_by>[a-zA_Z]+)/$', views.estados, name='estados'),
    url(r'^cidades/(?P<filter_by>[a-zA_Z]+)/$', views.cidades, name='cidades'),
    url(r'^países/(?P<filter_by>[a-zA_Z]+)/$', views.paíss, name='paíss'),
    url(r'^climas/(?P<filter_by>[a-zA_Z]+)/$', views.climas, name='climas'),
    url(r'^ambientes/(?P<filter_by>[a-zA_Z]+)/$', views.ambientes, name='ambientes'),

    # edição das amostras e perfis de usuarios /
    url(r'^amostra/(?P<pk>\d+)/update/$', views.amostraupdate.as_view(), name='amostraupdate'),
    url(r'^continente/(?P<pk>\d+)/update/$', views.continenteupdate.as_view(), name='continenteupdate'),
    url(r'^país/(?P<pk>\d+)/update/$', views.paísupdate.as_view(), name='paísupdate'),
    url(r'^estado/(?P<pk>\d+)/update/$', views.estadoupdate.as_view(), name='estadoupdate'),
    url(r'^cidade/(?P<pk>\d+)/update/$', views.cidadeupdate.as_view(), name='cidadeupdate'),
    url(r'^clima/(?P<pk>\d+)/update/$', views.climaupdate.as_view(), name='climaupdate'),
    url(r'^ambiente/(?P<pk>\d+)/update/$', views.ambienteupdate.as_view(), name='ambienteupdate'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^change_password/$',views.change_password, name='change_password'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),

   # recuperação de senha  pelo usuario/
    url(r'^reset-password/$', password_reset,
        {'template_name': 'catalogação/reset_password.html', 'post_reset_redirect': 'catalogação:password_reset_done',
         'email_template_name': 'catalogação/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'catalogação/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'catalogação/reset_password_confirm.html',
         'post_reset_redirect': 'catalogação:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'catalogação/reset_password_complete.html'}, name='password_reset_complete'),

    # definições para campos autocomplete para as pesquisas e filtro para pesquisa avançada do sistema/
    url(r'^amostra/autocomplete/', views.amostras, name='amostras'),
    url(r'^grupo_dados/$', views.gru, name='gru'),
    url(r'^grupo/$', views.grupo, name='grupo'),
    url(r'^amostraFilter/$', FilterView.as_view(filterset_class=amostraFilter, template_name='catalogação/grupo.html'),
        name='amostraFilter'),

]

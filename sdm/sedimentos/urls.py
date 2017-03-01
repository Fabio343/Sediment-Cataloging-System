from django.conf.urls import url
from django.contrib.auth.views import   password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
app_name = 'sedimentos'

urlpatterns = [

   # se refere a detalhes gerais e apresentação inicial do site /
    url(r'^$', views.index, name='index'),
    url(r'^$', views.amostra, name='amostra'),

    # se refere a criação e exclusão de amostras/
    url(r'^(?P<amostra_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_amostra/$', views.create_amostra, name='create_amostra'),
    url(r'^(?P<amostra_id>[0-9]+)/delete_amostra/$', views.delete_amostra, name='delete_amostra'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # se refere a detalhes de criação e exclusão de continentes/
    url(r'^(?P<continente_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'continente/add/$', views.create_continente, name='create_continente'),
    url(r'continente/(?P<continente_id>[0-9]+)/$', views.delete_continente, name='delete_continente'),

    # se refere a detalhes de criação e exclusão de cidades/
    url(r'^(?P<cidade_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'cidade/add/$', views.create_cidade, name='create_cidade'),
    url(r'cidade/(?P<cidade_id>[0-9]+)/$', views.delete_cidade, name='delete_cidade'),

    # se refere a detalhes de criaçãoe exclusão de estados/
    url(r'^(?P<estado_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'estado/add/$', views.create_estado, name='create_estado'),
    url(r'estado/(?P<estado_id>[0-9]+)/$', views.delete_estado, name='delete_estado'),

    # se refere a detalhes de crianção e exclusão de paises/
    url(r'^(?P<país_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'país/add/$', views.create_país, name='create_país'),
    url(r'país/(?P<país_id>[0-9]+)/$', views.delete_país, name='delete_país'),

    # se refere a detalhes de criação  e exclusão de ambientes /
    url(r'^(?P<ambiente_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'ambiente/add/$', views.create_ambiente, name='create_ambiente'),
    url(r'ambiente/(?P<ambiente_id>[0-9]+)/$', views.delete_ambiente, name='delete_ambiente'),

    # se refere a detalhes de criação e exclusão de climas/
    url(r'^(?P<clima_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'clima/add/$', views.create_clima, name='create_clima'),
    url(r'clima/(?P<clima_id>[0-9]+)/$', views.delete_clima, name='delete_clima'),

    # se refere a login,cadastros,creditos e demais detalhes ao desenvolvimento/
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^inicial/$', views.inicial, name='inicial'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^adicionar/$', views.adicionar, name='adicionar'),
    url(r'^agradecimentos/$', views.agradecimentos, name='agradecimentos'),
    url(r'^register/$', views.register, name='register'),

    # filtros para as pesquisas de modo que aceita qualquer informação  de modo a levar ao usuario que realiza pesquisa
    # a melhor e mais proxima que seja a informação que ele se referiu/
    url(r'^continentes/(?P<filter_by>[a-zA_Z]+)/$', views.continentes, name='continentes'),
    url(r'^estados/(?P<filter_by>[a-zA_Z]+)/$', views.estados, name='estados'),
    url(r'^cidades/(?P<filter_by>[a-zA_Z]+)/$', views.cidades, name='cidades'),
    url(r'^paíss/(?P<filter_by>[a-zA_Z]+)/$', views.paíss, name='paíss'),
    url(r'^climas/(?P<filter_by>[a-zA_Z]+)/$', views.climas, name='climas'),
    url(r'^ambientes/(?P<filter_by>[a-zA_Z]+)/$', views.ambientes, name='ambientes'),
    url(r'^amostras/(?P<filter_by>[a-zA_Z]+)/$', views.amostras, name='amostras'),

    # edição de informações de amostras,contientes... visualização de informações de administradores , além da  recuperação de informações como senha/
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^amostra-edit/(?P<amostra_id>[0-9]+)/edit/$', views.amostra_edit, name='amostra_edit'),
    url(r'^continente-edit/(?P<continente_id>[0-9]+)/edit/$', views.continente_edit, name='continente_edit'),
    url(r'^país-edit/(?P<país_id>[0-9]+)/edit/$', views.país_edit, name='país_edit'),
    url(r'^estado-edit/(?P<estado_id>[0-9]+)/edit/$', views.estado_edit, name='estado_edit'),
    url(r'^cidade-edit/(?P<cidade_id>[0-9]+)/edit/$', views.cidade_edit, name='cidade_edit'),
    url(r'^clima-edit/(?P<clima_id>[0-9]+)/edit/$', views.clima_edit, name='clima_edit'),
    url(r'^ambiente-edit/(?P<ambiente_id>[0-9]+)/edit/$', views.ambiente_edit, name='ambiente_edit'),

    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^change_password/$',views.change_password, name='change_password'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),


    url(r'^reset-password/$', password_reset,
        {'template_name': 'sedimentos/reset_password.html', 'post_reset_redirect': 'sedimentos:password_reset_done',
         'email_template_name': 'sedimentos/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'sedimentos/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'sedimentos/reset_password_confirm.html',
         'post_reset_redirect': 'sedimentos:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'sedimentos/reset_password_complete.html'}, name='password_reset_complete'),



]
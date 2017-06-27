from django.shortcuts import  render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .models import Amostra
from .models import Continente
from .models import Cidade
from .models import Estado
from .models import País
from .models import Ambiente
from .models import Clima
from .forms import UserForm,amostraForm, continenteForm, paísForm, estadoForm, cidadeForm,climaForm,ambienteForm,EditProfileForm,FormContato
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
import json
from django.http import HttpResponse
from .filters import amostraFilter
from django.shortcuts import render
from django.views.generic.edit import UpdateView

#função para contato com administração
def contato(request):
    if request.method == 'POST':
        form = FormContato(request.POST)

        if form.is_valid():
            form.enviar()
            mostrar = 'Contato enviado!'
            form = FormContato()
    else:
        form = FormContato()
    return render(request,'catalogação/contato.html', locals())

########################################################################################################################
# todas a funções abaixo com o termo update são para e edição dos exemplares do sistema
class amostraupdate(UpdateView):
     model = Amostra
     fields = ['codigo', 'coletador', 'Contato', 'descrição', 'tipo', 'data', 'granulometria', 'imagem', 'imagem1',
          'imagem2', 'imagem3',
          'imagem4', 'imagem5', 'imagem6', 'imagem7', 'imagem8', 'Continentes', 'Paíss', 'Estados', 'Cidades',
          'Ambientes', 'Climas']

########################################################################################################################
class continenteupdate(UpdateView):
        model =Continente
        fields = [ 'nome', 'sigla']

########################################################################################################################
class paísupdate(UpdateView):
        model =País
        fields = [ 'nome', 'região','Continentes']

########################################################################################################################
class estadoupdate(UpdateView):
        model =Estado
        fields = [ 'nome','Continentes','Paíss']

########################################################################################################################
class cidadeupdate(UpdateView):
        model =Cidade
        fields = [ 'nome', 'geologia','Continentes','Paíss','Estados']

########################################################################################################################
class ambienteupdate(UpdateView):
        model =Ambiente
        fields = [ 'tipo','Continentes','Paíss','Estados','Cidades']

########################################################################################################################
class climaupdate(UpdateView):
        model =Clima
        fields = [ 'tipo','Continentes','Paíss','Estados','Cidades']

########################################################################################################################
def amostras(request):
  if request.is_ajax():
    q = request.GET.get('term')
    amostras = Amostra.objects.filter(codigo__icontains=q)
    results = []
    for amostra in amostras:
      amostra_json = {}
      amostra_json = amostra.codigo
      results.append(amostra_json)
      data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

########################################################################################################################
def grupo(request):
        grupo = amostraFilter(request.GET, queryset=Amostra.objects.all())
        return render(request, 'catalogação/grupo.html', {'filter': grupo})

########################################################################################################################
def gru(request):
    amostras=Amostra.objects.all()
    return render(request,
        "catalogação/gru.html",{'amostras':amostras} )
########################################################################################################################
# as funções abaixo definem como são criados os exemplares bem como sua exclusão e visualização de detalhes
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_amostra(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = amostraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.user = request.user
            amostra.save()
            return render(request, 'catalogação/detail.html', {'amostra': amostra})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/amostra_form.html', context)

def delete_amostra(request, amostra_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     amostra = Amostra.objects.get(pk=amostra_id)
     amostra.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})


def detail(request, amostra_id):
        user = request.user
        amostra = get_object_or_404(Amostra, pk=amostra_id)
        return render(request, 'catalogação/detail.html', {'amostra': amostra, 'user': user})

########################################################################################################################
########################################################################################################################

def create_continente(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = continenteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            continente = form.save(commit=False)
            continente.user = request.user
            continente.save()
            return render(request, 'catalogação/concluido.html', {continente: continente})
        context = {"form": form, }
        return render(request, 'catalogação/continente_form.html', context)


def delete_continente(request, continente_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     continente = Continente.objects.get(pk=continente_id)
     continente.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_cidade(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = cidadeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.user = request.user
            cidade.save()
            return render(request, 'catalogação/concluido.html', {cidade: cidade})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/cidade_form.html', context)


def delete_cidade(request, cidade_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     cidade = Cidade.objects.get(pk=cidade_id)
     cidade.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_estado(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = estadoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.user = request.user
            estado.save()
            return render(request, 'catalogação/concluido.html', {estado: estado})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/estado_form.html', context)


def delete_estado(request, estado_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     estado = Estado.objects.get(pk=estado_id)
     estado.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_país(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = paísForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            país = form.save(commit=False)
            país.user = request.user
            país.save()
            return render(request, 'catalogação/concluido.html', {país: país})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/país_form.html', context)


def delete_país(request, país_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     país = País.objects.get(pk=país_id)
     país.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_ambiente(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = ambienteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ambiente = form.save(commit=False)
            ambiente.user = request.user
            ambiente.save()
            return render(request, 'catalogação/concluido.html', {ambiente: ambiente})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/ambiente_form.html', context)


def delete_ambiente(request, ambiente_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     ambiente = Ambiente.objects.get(pk=ambiente_id)
     ambiente.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_clima(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
        form = climaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.user = request.user
            clima.save()
            return render(request, 'catalogação/concluido.html', {clima: clima})
        context = {
            "form": form,
        }
        return render(request, 'catalogação/clima_form.html', context)


def delete_clima(request, clima_id):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     clima = Clima.objects.get(pk=clima_id)
     clima.delete()
     return render(request, 'catalogação/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################
# função de pagina inicial e pesquisa simples
def index(request):
        amostras = Amostra.objects.filter()
        país_results = País.objects.all()
        amostra_results = Amostra.objects.all()
        continente_results = Continente.objects.all()
        estado_results = Estado.objects.all()
        cidade_results = Cidade.objects.all()
        clima_results = Clima.objects.all()
        ambiente_results = Ambiente.objects.all()
        amostra_list = Amostra.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(amostra_list, 24)


        try:
            amostras = paginator.page(page)
        except PageNotAnInteger:
            amostras = paginator.page(1)
        except EmptyPage:
            amostras= paginator.page(paginator.num_pages)


        query = request.GET.get("q")
        if query:
            amostra_results = amostra_results.filter(
                Q(codigo__icontains=query) |
                Q(tipo__icontains=query) |
                Q(descrição__icontains=query) |
                Q(coletador__icontains=query) |
                Q(granulometria__icontains=query) |
                Q(data__icontains=query)
            ).distinct()
            país_results = país_results.filter(
                Q(nome__icontains=query)
            ).distinct()
            continente_results = continente_results.filter(
                Q(nome__icontains=query)

            ).distinct()
            estado_results = estado_results.filter(
                Q(nome__icontains=query)
            ).distinct()
            cidade_results = cidade_results.filter(
                Q(nome__icontains=query) |
                Q(geologia__icontains=query)
            ).distinct()
            clima_results = clima_results.filter(
                Q(tipo__icontains=query)
            ).distinct()
            ambiente_results = ambiente_results.filter(
                Q(tipo__icontains=query)
            ).distinct()
            return render(request, 'catalogação/pesquisa.html', {
                'amostras': amostras,
                'paíss': país_results,
                'continentes': continente_results,
                'estados': estado_results,
                'cidades': cidade_results,
                'climas': clima_results,
                'ambientes': ambiente_results,
                'amostras': amostra_results,

            })
        else:
            return render(request, 'catalogação/index.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################
# função de pagina inicial e pesquisa simples
def amostra(request):
        amostras = Amostra.objects.filter()
        país_results = País.objects.all()
        amostra_results = Amostra.objects.all()
        continente_results = Continente.objects.all()
        estado_results = Estado.objects.all()
        cidade_results = Cidade.objects.all()
        clima_results = Clima.objects.all()
        ambiente_results = Ambiente.objects.all()

        query = request.GET.get("q")
        if query:
            amostras = amostras.filter(
                Q(codigo__icontains=query) |
                Q(tipo__icontains=query) |
                Q(descrição__icontains=query) |
                Q(coletador__icontains=query) |
                Q(granulometria__icontains=query) |
                Q(data__icontains=query)
            ).distinct()
            país_results = país_results.filter(
                Q(nome__icontains=query)
            ).distinct()
            continente_results = continente_results.filter(
                Q(americano__icontains=query) |
                Q(sigla__icontains=query)
            ).distinct()
            estado_results = estado_results.filter(
                Q(nome__icontains=query)
            ).distinct()
            cidade_results = cidade_results.filter(
                Q(nome__icontains=query) |
                Q(geologia__icontains=query)
            ).distinct()
            clima_results = clima_results.filter(
                Q(tipo__icontains=query)
            ).distinct()
            ambiente_results = ambiente_results.filter(
                Q(tipo__icontains=query)
            ).distinct()
            return render(request, 'catalogação/pesquisa.html', {
                'amostras': amostras,
                'paíss': país_results,
                'continentes': continente_results,
                'estados': estado_results,
                'cidades': cidade_results,
                'climas': clima_results,
                'ambientes': ambiente_results,
                'amostras': amostra_results,

            })
        else:
            return render(request, 'catalogação/amostra.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################
#fubnção que define a chamada de forms ou seja define as formas de campos atribuidas pelos templates
class UserFormView(View):
    form_class=UserForm
    template_name='catalogação/register_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password,first_name=first_name,last_name=last_name)

            if user is not None:

                if user.is_active:
                    login(request,user)
                return redirect('catalogação:index')
        return render(request, self.template_name, {'form': form})

########################################################################################################################
########################################################################################################################
# função para desconectar do sistema
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'catalogação/logout.html', context)

########################################################################################################################
########################################################################################################################
#função de pagina inicial
def inicial(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'catalogação/index.html', context)

########################################################################################################################
########################################################################################################################
# função que define a chamada de pagina de login de usuario
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                amostras = Amostra.objects.filter(user=request.user)
                return render(request, 'catalogação/index.html', {'amostras': amostras})
            else:
                return render(request, 'catalogação/login.html', {'error_message': 'Sua conta foi desativada'})
        else:
                return render(request, 'catalogação/login.html', {'error_message': ' Login Invalido '})
    return render(request, 'catalogação/login.html')

########################################################################################################################
########################################################################################################################
#função de registro de usuarios
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                amostras = Amostra.objects.filter(user=request.user)
                return render(request, 'catalogação/index.html', {'amostras': amostras})
    context = {
        "form": form,
    }
    return render(request, 'catalogação/register_form.html', context)

########################################################################################################################
########################################################################################################################
#função que direciona para a pagina de seleção de criação de alguma informação ou exemplar
def adicionar(request):
    if not request.user.is_authenticated():
        return render(request, 'catalogação/login.html')
    else:
     form = UserForm(request.POST or None)
     context = {
        "form": form,
        }
    return render(request, 'catalogação/adicionar.html', context)

########################################################################################################################
########################################################################################################################
# função para direcionar a pagina de creditos de desenvolvimento
def agradecimentos(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'catalogação/agradecimentos.html', context)
########################################################################################################################
########################################################################################################################
# as funções abaixo definem os filtros da pesquisa simples
def continentes(request, filter_by):
        try:
            continente_ids = []
            for continente in Continente.objects.filter():

                for continente in continente.amostra_set.all():
                    continente_ids.append(continente.pk)

            users_continentes = Continente.objects.filter(pk__in=continente_ids)

            if filter_by == 'favorites':
                users_continentes = users_continentes.filter(is_favorite=True)
        except Continente.DoesNotExist:
            users_continentes = []

        return render(request, 'catalogação/continentes.html', {
            'continente_list': users_continentes,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################

def paíss(request, filter_by):
        try:
            país_ids = []
            for país in País.objects.filter():
                for país in país.amostra_set.all():
                    país_ids.append(país.pk)
            users_paíss = País.objects.filter(pk__in=país_ids)
            if filter_by == 'favorites':
                users_paíss = users_paíss.filter(is_favorite=True)
        except País.DoesNotExist:
            users_paíss = []
        return render(request, 'catalogação/paíss.html', {
            'país_list': users_paíss,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################

def estados(request, filter_by):
        try:
            estado_ids = []
            for estado in Estado.objects.filter():
                for estado in estado.amostra_set.all():
                    estado_ids.append(estado.pk)
            users_estados = Estado.objects.filter(pk__in=estado_ids)
            if filter_by == 'favorites':
                users_estados = users_estados.filter(is_favorite=True)
        except Estado.DoesNotExist:
            users_estados = []
        return render(request, 'catalogação/estados.html', {
            'estado_list': users_estados,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################

def cidades(request, filter_by):
        try:
            cidade_ids = []
            for cidade in Cidade.objects.filter():
                for cidade in cidade.amostra_set.all():
                    cidade_ids.append(cidade.pk)
            users_cidades = Cidade.objects.filter(pk__in=cidade_ids)
            if filter_by == 'favorites':
                users_cidades = users_cidades.filter(is_favorite=True)
        except Cidade.DoesNotExist:
            users_cidades = []
        return render(request, 'catalogação/cidades.html', {
            'cidade_list': users_cidades,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################

def climas(request, filter_by):
        try:
            clima_ids = []
            for clima in Clima.objects.filter():
                for clima in clima.amostra_set.all():
                    clima_ids.append(clima.pk)
            users_climas = Clima.objects.filter(pk__in=clima_ids)
            if filter_by == 'favorites':
                users_climas = users_climas.filter(is_favorite=True)
        except Clima.DoesNotExist:
            users_climas = []
        return render(request, 'catalogação/climas.html', {
            'clima_list': users_climas,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################

def ambientes(request, filter_by):
        try:
            ambiente_ids = []
            for ambiente in Ambiente.objects.filter():
                for ambiente in ambiente.amostra_set.all():
                    ambiente_ids.append(ambiente.pk)
            users_ambientes = Ambiente.objects.filter(pk__in=ambiente_ids)
            if filter_by == 'favorites':
                users_ambientes = users_ambientes.filter(is_favorite=True)
        except Ambiente.DoesNotExist:
            users_ambientes = []
        return render(request, 'catalogação/ambientes.html', {
            'ambiente_list': users_ambientes,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
#função para conclução de edição de exemplares
def edit(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'catalogação/edit.html', context)

########################################################################################################################
########################################################################################################################
#as 2 funções  abaixo para a visualização de perfil de usuario e de recuperação de informações no casoc senha
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('catalogação/login.html'))
        else:
            return redirect(reverse('catalogação/change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'catalogação/change_password.html', args)

########################################################################################################################
########################################################################################################################

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'catalogação/profile.html', args)

########################################################################################################################
########################################################################################################################
# edição de perfil
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('catalogação:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'catalogação/edit_profile.html', args)
########################################################################################################################


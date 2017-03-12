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
from .forms import UserForm,ContactForm, ContatoForm, amostraForm, continenteForm, paísForm, estadoForm, cidadeForm,climaForm,ambienteForm,EditProfileForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
#from .filters import amostraFilter

#def filtro(request):
#    amostra_list=Amostra.objects.all()
 #   amostra_filter=amostraFilter(request.GET,queryset=amostra_list)
  #  return render(request,'sedimentos/amostra_list.html',{' filter':amostra_filter})

def lista_continente(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_continente.html",{'amostras':amostras, 'user': user} )

def lista_país(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_país.html",{'amostras':amostras, 'user': user} )

def lista_estado(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_estado.html",{'amostras':amostras, 'user': user} )

def lista_cidade(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_cidade.html",{'amostras':amostras, 'user': user} )

def lista_ambiente(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_ambiente.html",{'amostras':amostras, 'user': user} )

def lista_clima(request):
    user = request.user
    amostras=Amostra.objects.all()
    return render_to_response(
        "amostras/lista_clima.html",{'amostras':amostras, 'user': user} )
########################################################################################################################


########################################################################################################################
def autoamostras(request):
    if request.is_ajax:
        search = request.GET.get('start', '')
        amostras = Amostra.objects.filter(codigo__icontains=search)
        results = []
        for amostra in amostras:
            amostra_json = {}
            amostra_json['id'] = amostra.id
            amostra_json['codigo'] = amostra.codigo
            results.append(amostra_json)
        data_json = json.dumps(results)
    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)

########################################################################################################################
def autopais(request):
    if request.is_ajax:
        search = request.GET.get('start', '')
        paíss = País.objects.filter(nome__icontains=search)
        results = []
        for país in paíss:
            país_json = {}
            país_json['label'] = país.nome
            país_json['value'] = país.nome
            results.append(país_json)
        data_json = json.dumps(results)
    else:
        data_json = 'fail'
    mimetype = "amostras/json"
    return HttpResponse(data_json, mimetype)

########################################################################################################################
def autoestado(request):
    if request.is_ajax:
        search = request.POST.get('start', '')

        estados = Estado.objects.filter(nome__icontains=search)

        results = []
        for estado in estados:
            estado_json = {}
            estado_json['label'] = estado.nome
            estado_json['value'] = estado.nome
            results.append(estado_json)

        data_json = json.dumps(results)

    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)

########################################################################################################################
def autocidade(request):
    if request.is_ajax:
        search = request.POST.get('start', '')

        cidades = Cidade.objects.filter(nome__icontains=search)

        results = []
        for cidade in cidades:
            cidade_json = {}
            cidade_json['label'] = cidade.nome
            cidade_json['value'] = cidade.nome
            results.append(cidade_json)

        data_json = json.dumps(results)

    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)

########################################################################################################################
def autoambiente(request):
    if request.is_ajax:
        search = request.POST.get('start', '')
        ambientes = Ambiente.objects.filter(tipo__icontains=search)
        results = []
        for ambiente in ambientes:
            ambiente_json = {}
            ambiente_json['label'] = ambiente.tipo
            ambiente_json['value'] = ambiente.tipo
            results.append(ambiente_json)

        data_json = json.dumps(results)

    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)



########################################################################################################################
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_amostra(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = amostraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.user = request.user
            amostra.save()
            return render(request, 'amostras/detail.html', {'amostra': amostra})
        context = {
            "form": form,
        }
        return render(request, 'amostras/amostra_form.html', context)

def delete_amostra(request, amostra_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     amostra = Amostra.objects.get(pk=amostra_id)
     amostra.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})


def detail(request, amostra_id):
        user = request.user
        amostra = get_object_or_404(Amostra, pk=amostra_id)
        return render(request, 'amostras/detail.html', {'amostra': amostra, 'user': user})

########################################################################################################################
########################################################################################################################

def create_continente(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = continenteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            continente = form.save(commit=False)
            continente.user = request.user
            continente.save()
            return render(request, 'amostras/detail.html', {continente: continente})
        context = {
            "form": form,
        }
        return render(request, 'amostras/continente_form.html', context)


def delete_continente(request, continente_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     continente = Continente.objects.get(pk=continente_id)
     continente.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_cidade(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = cidadeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.user = request.user
            cidade.save()
            return render(request, 'amostras/detail.html', {cidade: cidade})
        context = {
            "form": form,
        }
        return render(request, 'amostras/cidade_form.html', context)


def delete_cidade(request, cidade_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     cidade = Cidade.objects.get(pk=cidade_id)
     cidade.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_estado(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = estadoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.user = request.user
            estado.save()
            return render(request, 'amostras/detail.html', {estado: estado})
        context = {
            "form": form,
        }
        return render(request, 'amostras/estado_form.html', context)


def delete_estado(request, estado_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     estado = Estado.objects.get(pk=estado_id)
     estado.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_país(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = paísForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            país = form.save(commit=False)
            país.user = request.user
            país.save()
            return render(request, 'amostras/detail.html', {país: país})
        context = {
            "form": form,
        }
        return render(request, 'amostras/país_form.html', context)


def delete_país(request, país_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     país = País.objects.get(pk=país_id)
     país.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_ambiente(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = ambienteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ambiente = form.save(commit=False)
            ambiente.user = request.user
            ambiente.save()
            return render(request, 'amostras/detail.html', {ambiente: ambiente})
        context = {
            "form": form,
        }
        return render(request, 'amostras/ambiente_form.html', context)


def delete_ambiente(request, ambiente_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     ambiente = Ambiente.objects.get(pk=ambiente_id)
     ambiente.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

def create_clima(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
        form = climaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.user = request.user
            clima.save()
            return render(request, 'amostras/detail.html', {clima: clima})
        context = {
            "form": form,
        }
        return render(request, 'amostras/clima_form.html', context)


def delete_clima(request, clima_id):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     clima = Clima.objects.get(pk=clima_id)
     clima.delete()
     return render(request, 'amostras/delete.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

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
            amostras = paginator.page(paginator.num_pages)

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
                Q(nome__icontains=query) |
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
            return render(request, 'amostras/pesquisa.html', {
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
            return render(request, 'amostras/index.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

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
                Q(nome__icontains=query) |
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
            return render(request, 'amostras/pesquisa.html', {
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
            return render(request, 'amostras/amostra.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################

class UserFormView(View):
    form_class=UserForm
    template_name='amostras/register_form.html'

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
                return redirect('amostras:index')
        return render(request, self.template_name, {'form': form})

########################################################################################################################
########################################################################################################################

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'amostras/logout.html', context)

########################################################################################################################
########################################################################################################################

def inicial(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'amostras/inicial.html', context)

########################################################################################################################
########################################################################################################################

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                amostras = Amostra.objects.filter(user=request.user)
                return render(request, 'amostras/inicial.html', {'amostras': amostras})
            else:
                return render(request, 'amostras/login.html', {'error_message': 'Sua conta foi desativada'})
        else:
                return render(request, 'amostras/login.html', {'error_message': ' Login Invalido '})
    return render(request, 'amostras/login.html')

########################################################################################################################
########################################################################################################################

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
                return render(request, 'amostras/index.html', {'amostras': amostras})
    context = {
        "form": form,
    }
    return render(request, 'amostras/register_form.html', context)

########################################################################################################################
########################################################################################################################

def contato(request):
    form_class = ContatoForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            Nome = request.POST.get('Nome', '')
            Email = request.POST.get('Email', '')
            Mensagem = request.POST.get('Mensagem', '')
            template = get_template('amostras/contato.html')
            context = Context({
                'Nome': Nome,
                'Email': Email,
                'Mensagem': Mensagem,
            })
            content = template.render(context)
            email =EmailMessage (
                "New contact form submission", content, "Adiministração" + '', ['fabio.carvalho.souza@usp.br'],
                headers={'Reply-To': Email}
            )
            email.send()
            return redirect('contato')
    return render(request, 'amostras/contato.html', {'form': form_class, })

########################################################################################################################
########################################################################################################################

def adicionar(request):
    if not request.user.is_authenticated():
        return render(request, 'amostras/login.html')
    else:
     form = UserForm(request.POST or None)
     context = {
        "form": form,
        }
    return render(request, 'amostras/adicionar.html', context)

########################################################################################################################
########################################################################################################################

def agradecimentos(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'amostras/agradecimentos.html', context)

########################################################################################################################
########################################################################################################################
def amostras(request, filter_by):
        try:
            amostra_ids = []
            for amostra in Amostra.objects.filter():
                for amostra in amostra.amostra_set.all():
                    amostra_ids.append(amostra.pk)
            users_amostras = Amostra.objects.filter(pk__in=amostra_ids)
            if filter_by == 'favorites':
                users_amostras = users_amostras.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_amostras = []
        return render(request, 'amostras/amostras.html', {
            'amostra_list': users_amostras,
            'filter_by': filter_by,
        })


########################################################################################################################
########################################################################################################################

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

    return render(request, 'amostras/continentes.html', {
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
    return render(request, 'amostras/paíss.html', {
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
    return render(request, 'amostras/estados.html', {
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
    return render(request, 'amostras/cidades.html', {
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
    return render(request, 'amostras/climas.html', {
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
    return render(request, 'amostras/ambientes.html', {
        'ambiente_list': users_ambientes,
        'filter_by': filter_by,
    })


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

def edit(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'amostras/edit.html', context)

########################################################################################################################
########################################################################################################################
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('amostras/login.html'))
        else:
            return redirect(reverse('amostras/change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'amostras/change_password.html', args)

########################################################################################################################
########################################################################################################################

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'amostras/profile.html', args)

########################################################################################################################
########################################################################################################################
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('amostras:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'amostras/edit_profile.html', args)

########################################################################################################################
########################################################################################################################
def amostra_edit(request,amostra_id):
    amostra = get_object_or_404(Amostra,pk=amostra_id)
    if request.method == "POST":
        form =amostraForm(request.POST, instance=amostra)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = amostraForm(instance=amostra)
    return render(request, 'amostras/amostra_edit.html', {'form': form})
########################################################################################################################
########################################################################################################################
def continente_edit(request,continente_id):
    continente = get_object_or_404(Continente,pk=continente_id)
    if request.method == "POST":
        form =continenteForm(request.POST, instance=continente)
        if form.is_valid():
            continente = form.save(commit=False)
            continente.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = continenteForm(instance=continente)
    return render(request, 'amostras/continente_edit.html', {'form': form})

########################################################################################################################
########################################################################################################################
def país_edit(request,país_id):
    país = get_object_or_404(País,pk=país_id)
    if request.method == "POST":
        form =paísForm(request.POST, instance=país)
        if form.is_valid():
            país = form.save(commit=False)
            país.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = paísForm(instance=país)
    return render(request, 'amostras/país_edit.html', {'form': form})

########################################################################################################################
########################################################################################################################
def estado_edit(request,estado_id):
    estado = get_object_or_404(Estado,pk=estado_id)
    if request.method == "POST":
        form =estadoForm(request.POST, instance=estado)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = estadoForm(instance=estado)
    return render(request, 'amostras/estado_edit.html', {'form': form})


########################################################################################################################
########################################################################################################################
def cidade_edit(request,cidade_id):
    cidade = get_object_or_404(Cidade,pk=cidade_id)
    if request.method == "POST":
        form =cidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = cidadeForm(instance=cidade)
    return render(request, 'amostras/cidade_edit.html', {'form': form})

########################################################################################################################
########################################################################################################################
def clima_edit(request,clima_id):
    clima = get_object_or_404(Clima,pk=clima_id)
    if request.method == "POST":
        form =climaForm(request.POST, instance=clima)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = climaForm(instance=clima)
    return render(request, 'amostras/clima_edit.html', {'form': form})

########################################################################################################################
########################################################################################################################
def ambiente_edit(request,ambiente_id):
    ambiente = get_object_or_404(Ambiente,pk=ambiente_id)
    if request.method == "POST":
        form =ambienteForm(request.POST, instance=ambiente)
        if form.is_valid():
            ambiente = form.save(commit=False)
            ambiente.save()
            return redirect(reverse('amostras:inicial'))

    else:
        form = ambienteForm(instance=ambiente)
    return render(request, 'amostras/ambiente_edit.html', {'form': form})





def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            Nome = request.POST.get(
                'Nome'
            , '')
            Email = request.POST.get(
                'Email'
            , '')
            Mensagem = request.POST.get('content', '')
            template =  get_template('amostras/contac_template.txt')
            context = Context({
                'Nome': Nome,
                'Email': Email,
                'Mensagem': Mensagem,
            })
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['fabio.carvalho.souza@usp.br'],
                headers = {'Reply-To': Email }
            )
            email.send(

            )
            return render(request, 'amostras/inicial.html', context)
    return render(request, 'amostras/contact.html', { 'form': form_class, })




#class AutoCompleteView(FormView):
 #   def get(self,request,*args,**kwargs):
  #      amostra = request.GET
   #     username = amostra.get("term")
    #    if username:
     #      users = User.objects.filter(username__icontain s= username)
      #    else:
       #       users = User.objects.all()
        #      results = []
       # for amostra in amostras:
        #    user_json = {}
         #   user_json['id'] = user.id
          #  user_json['label'] = user.username
           # user_json['value'] = user.username
            #results.append(user_json)
           # data = json.dumps(results)
           # mimetype = 'application/json'
       # return HttpResponse(data, mimetype)


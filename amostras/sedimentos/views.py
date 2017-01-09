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
from .forms import UserForm, ContatoForm, amostraForm, continenteForm, paísForm, estadoForm, cidadeForm,climaForm,ambienteForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.db.models import Q


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_amostra(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = amostraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            amostra = form.save(commit=False)
            amostra.user = request.user
            amostra.imagem = request.FILES['imagem']
            file_type = amostra.imagem.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'amostra': amostra,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'sedimentos/amostra_form.html', context)
            amostra.save()
            return render(request, 'sedimentos/detail.html', {'amostra': amostra})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/amostra_form.html', context)



def delete_amostra(request, amostra_id):
    amostra = Amostra.objects.get(pk=amostra_id)
    amostra.delete()
    amotras = amostra.objects.filter(user=request.user)
    return render(request, 'sedimentos/index.html', {'amostras': amotras})

def detail(request, amostra_id):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        user = request.user
        amostra = get_object_or_404(Amostra, pk=amostra_id)
        return render(request, 'sedimentos/detail.html', {'amostra': amostra, 'user': user})



########################################################################################################################
########################################################################################################################
########################################################################################################################

def create_continente(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = continenteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            continente = form.save(commit=False)
            continente.user = request.user
            continente.save()
            return render(request, 'sedimentos/detail.html', {continente: continente})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/continente_form.html', context)


def delete_continente(request, continente_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    continente = Continente.objects.get(pk=continente_id)
    continente.delete()
    return render(request, 'sedimentos/index.html', {'amostra':amostra})


########################################################################################################################
########################################################################################################################
########################################################################################################################



def create_cidade(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = cidadeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.user = request.user
            cidade.save()
            return render(request, 'sedimentos/detail.html', {cidade: cidade})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/cidade_form.html', context)


def delete_cidade(request, cidade_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    cidade = Cidade.objects.get(pk=cidade_id)
    cidade.delete()
    return render(request, 'sedimentos/index.html', {'amostra': amostra})


########################################################################################################################
########################################################################################################################
########################################################################################################################


def create_estado(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = estadoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.user = request.user
            estado.save()
            return render(request, 'sedimentos/detail.html', {estado: estado})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/estado_form.html', context)


def delete_estado(request, estado_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    estado = Estado.objects.get(pk=estado_id)
    estado.delete()
    return render(request, 'sedimentos/index.html', {'amostra': amostra})
########################################################################################################################
########################################################################################################################
########################################################################################################################



def create_país(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = paísForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            país = form.save(commit=False)
            país.user = request.user
            país.save()
            return render(request, 'sedimentos/detail.html', {país: país})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/país_form.html', context)


def delete_país(request, país_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    país = País.objects.get(pk=país_id)
    país.delete()
    return render(request, 'sedimentos/index.html', {'amostra': amostra})

########################################################################################################################
########################################################################################################################
########################################################################################################################

def create_ambiente(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = ambienteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ambiente = form.save(commit=False)
            ambiente.user = request.user
            ambiente.save()
            return render(request, 'sedimentos/detail.html', {ambiente: ambiente})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/ambiente_form.html', context)


def delete_ambiente(request, ambiente_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    ambiente = Ambiente.objects.get(pk=ambiente_id)
    ambiente.delete()
    return render(request, 'sedimentos/index.html', {'amostra': amostra})

########################################################################################################################
########################################################################################################################
########################################################################################################################

def create_clima(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        form = climaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.user = request.user
            clima.save()
            return render(request, 'sedimentos/detail.html', {clima: clima})
        context = {
            "form": form,
        }
        return render(request, 'sedimentos/clima_form.html', context)


def delete_clima(request, clima_id):
    amostra = get_object_or_404(Amostra, pk=amostra_id)
    clima = Clima.objects.get(pk=clima_id)
    clima.delete()
    return render(request, 'sedimentos/index.html', {'amostra': amostra})

########################################################################################################################
########################################################################################################################
########################################################################################################################
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        amostras = Amostra.objects.filter(user=request.user)
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
            return render(request, 'sedimentos/index.html', {
                'amotras': amostras,
                'paíss': país_results,
                'continentes': continente_results,
                'estados': estado_results,
                'cidades': cidade_results,
                'climas': clima_results,
                'ambientes': ambiente_results,
                'amostras': amostra_results,

            })
        else:
            return render(request, 'sedimentos/index.html', {'amostras': amostras})

########################################################################################################################
########################################################################################################################
########################################################################################################################
class UserFormView(View):
    form_class=UserForm
    template_name='sedimentos/register_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                return redirect('sedimentos:index')
        return render(request, self.template_name, {'form': form})

########################################################################################################################
########################################################################################################################
########################################################################################################################
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'sedimentos/login.html', context)

########################################################################################################################
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
                return render(request, 'sedimentos/index.html', {'amostras': amostras})
            else:
                return render(request, 'sedimentos/login.html', {'error_message': 'Sua conta foi desativada'})
        else:
                return render(request, 'sedimentos/login.html', {'error_message': ' Login Invalido '})
    return render(request, 'sedimentos/login.html')

########################################################################################################################
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
                return render(request, 'sedimentos/index.html', {'amostras': amostras})
    context = {
        "form": form,
    }
    return render(request, 'sedimentos/register_form.html', context)

########################################################################################################################
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
            template = get_template('sedimentos/contato.html')
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
    return render(request, 'sedimentos/contato.html', {'form': form_class, })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def adicionar(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'sedimentos/adicionar.html', context)


########################################################################################################################
########################################################################################################################
########################################################################################################################
def amostras(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            amostra_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for amostra in amostra.amostra_set.all():
                    amostra_ids.append(amostra.pk)
            users_amostras = Amostra.objects.filter(pk__in=amostra_ids)
            if filter_by == 'favorites':
                users_amostras = users_amostras.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_amostras = []
        return render(request, 'sedimentos/amostras.html', {
            'amostra_list': users_amostras,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
########################################################################################################################
def continentes(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            continente_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for continente in amostra.continente_set.all():
                    continente_ids.append(continente.pk)
            users_continentes = Continente.objects.filter(pk__in=continente_ids)
            if filter_by == 'favorites':
                users_continentes = users_continentes.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_continentes = []
        return render(request, 'sedimentos/continentes.html', {
            'continente_list': users_continentes,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def paíss(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            país_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for país in amostra.país_set.all():
                    país_ids.append(país.pk)
            users_paíss = País.objects.filter(pk__in=país_ids)
            if filter_by == 'favorites':
                users_paíss = users_paíss.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_paíss = []
        return render(request, 'sedimentos/paíss.html', {
            'país_list': users_paíss,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################
def estados(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            estado_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for estado in amostra.estado_set.all():
                    estado_ids.append(estado.pk)
            users_estados = Estado.objects.filter(pk__in=estado_ids)
            if filter_by == 'favorites':
                users_estados = users_estados.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_estados = []
        return render(request, 'sedimentos/estados.html', {
            'estado_list': users_estados,
            'filter_by': filter_by,
        })

########################################################################################################################
########################################################################################################################
########################################################################################################################

def cidades(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            cidade_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for cidade in amostra.cidade_set.all():
                    cidade_ids.append(cidade.pk)
            users_cidades = Cidade.objects.filter(pk__in=cidade_ids)
            if filter_by == 'favorites':
                users_cidades = users_cidades.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_cidades = []
        return render(request, 'sedimentos/cidades.html', {
            'cidade_list': users_cidades,
            'filter_by': filter_by,
        })


########################################################################################################################
########################################################################################################################
########################################################################################################################
def climas(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            clima_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for clima in amostra.clima_set.all():
                    clima_ids.append(clima.pk)
            users_climas = Clima.objects.filter(pk__in=clima_ids)
            if filter_by == 'favorites':
                users_climas = users_climas.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_climas = []
        return render(request, 'sedimentos/climas.html', {
            'clima_list': users_climas,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
########################################################################################################################
def ambientes(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'sedimentos/login.html')
    else:
        try:
            ambiente_ids = []
            for amostra in Amostra.objects.filter(user=request.user):
                for ambiente in amostra.ambiente_set.all():
                    ambiente_ids.append(ambiente.pk)
            users_ambientes = Ambiente.objects.filter(pk__in=ambiente_ids)
            if filter_by == 'favorites':
                users_ambientes = users_ambientes.filter(is_favorite=True)
        except Amostra.DoesNotExist:
            users_ambientes = []
        return render(request, 'sedimentos/ambientes.html', {
            'ambiente_list': users_ambientes,
            'filter_by': filter_by,
        })
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
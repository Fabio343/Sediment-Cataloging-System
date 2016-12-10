from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import  render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from .models import Amostra
from .models import  Continente
from .models import  Cidade
from .models import  Estado
from .models import  País
from .models import  Ambiente
from .models import Clima
from .forms import UserForm



class IndexView(generic.ListView):
    template_name = 'amostra/index.html'
    context_object_name = 'all_amostras'


    def get_queryset(self):

       return Amostra.objects.all()


class DetailView(generic.DetailView):
    model = Amostra
    template_name = 'amostra/detail.html'


class amostraCreate(CreateView):
    model = Amostra
    fields = ['codigo','coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem','imagem2']



class amostraUpdate(UpdateView ):
     model = Amostra
     fields = ['codigo', 'coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem','imagem2']


class amostraDelete(DeleteView):
    model=Amostra
    sucess_url=reverse_lazy('amostra:index')

########################################################################################################################

class IndexView2(generic.ListView):
    template_name = 'amostra/index2.html'
    context_object_name = 'all_continentes'

    def get_queryset(self):

       return Continente.objects.all()


class DetailView2(generic.DetailView):
    model = Continente
    template_name = 'amostra/detail2.html'


class continenteCreate(CreateView):
    model = Continente
    fields = ['Amostra','nome','sigla']



class continenteUpdate(UpdateView ):
     model = Continente
     fields = ['Amostra','nome','sigla']


class continenteDelete(DeleteView):
    model=Continente
    sucess_url=reverse_lazy('amostra:index2')
########################################################################################################################
class IndexView3(generic.ListView):
    template_name = 'amostra/index3.html'
    context_object_name = 'all_cidades'

    def get_queryset(self):

       return Cidade.objects.all()


class DetailView3(generic.DetailView):
    model = Cidade
    template_name = 'amostra/detail5.html'


class cidadeCreate(CreateView):
    model = Cidade
    fields = ['Amostra','Continente','País','Estado','nome','geologia']



class cidadeUpdate(UpdateView ):
     model = Cidade
     fields = ['Amostra','Continente','País','Estado','nome','geologia']


class cidadeDelete(DeleteView):
    model=Cidade
    sucess_url=reverse_lazy('amostra:index3')



########################################################################################################################

class IndexView4(generic.ListView):
    template_name = 'amostra/index4.html'
    context_object_name = 'all_estados'

    def get_queryset(self):

       return Estado.objects.all()


class DetailView4(generic.DetailView):
    model = Estado
    template_name = 'amostra/detail4.html'


class estadoCreate(CreateView):
    model = Estado
    fields = ['Amostra','Continente','País','nome']



class estadoUpdate(UpdateView ):
     model = Estado
     fields = ['Amostra','Continente','País','nome']


class estadoDelete(DeleteView):
    model=Estado
    sucess_url=reverse_lazy('amostra:index4')
########################################################################################################################

class IndexView5(generic.ListView):
    template_name = 'amostra/index5.html'
    context_object_name = 'all_paíss'

    def get_queryset(self):

       return País.objects.all()


class DetailView5(generic.DetailView):
    model = País
    template_name = 'amostra/detail3.html'


class paísCreate(CreateView):
    model = País
    fields = ['Amostra','Continente','nome', 'região']



class paísUpdate(UpdateView ):
     model = País
     fields = ['Amostra','Continente','nome', 'região']


class paísDelete(DeleteView):
    model=País
    sucess_url=reverse_lazy('amostra:index5')

########################################################################################################################
class IndexView6(generic.ListView):
    template_name = 'amostra/index6.html'
    context_object_name = 'all_ambientes'

    def get_queryset(self):

       return Ambiente.objects.all()


class DetailView6(generic.DetailView):
    model = Ambiente
    template_name = 'amostra/detail6.html'


class ambienteCreate(CreateView):
    model = Ambiente
    fields =  ['Amostra','Continente','País','Estado','Cidade','tipo']



class ambienteUpdate(UpdateView ):
     model = Ambiente
     fields =  ['Amostra','Continente','País','Estado','Cidade','tipo']


class ambienteDelete(DeleteView):
    model=Ambiente
    sucess_url=reverse_lazy('amostra:index6')

########################################################################################################################
class IndexView7(generic.ListView):
    template_name = 'amostra/index7.html'
    context_object_name = 'all_climas'

    def get_queryset(self):

       return Clima.objects.all()


class DetailView7(generic.DetailView):
    model = Clima
    template_name = 'amostra/detail7.html'


class climaCreate(CreateView):
    model = Clima
    fields =  ['Amostra','Continente','País','Estado','Cidade','tipo']



class climaUpdate(UpdateView ):
     model = Clima
     fields = ['Amostra','Continente','País','Estado','Cidade','tipo']


class climaDelete(DeleteView):
    model=Clima
    sucess_url=reverse_lazy('amostra:index7')
########################################################################################################################
class UserFormView(View):
    form_class=UserForm
    template_name='amostra/registration_form.html'

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
                return redirect('amostra:index')

        return render(request, self.template_name, {'form': form})
########################################################################################################################
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        }
    return render(request, 'amostra/login.html', context)
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
                return render(request, 'amostra/index.html', {'amostras': amostras})
            else:
                return render(request, 'amostra/login.html', {'error_message': 'Your account has been disabled'})
        else:
                return render(request, 'amostra/login.html', {'error_message': 'Invalid login'})

    return render(request, 'amostra/login.html')
########################################################################################################################
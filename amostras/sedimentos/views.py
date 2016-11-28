from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import  render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import amostra, continente, cidade, estado, país, ambiente, clima
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'sedimentos/index.html'
    context_object_name = 'all_amostras'

    def get_queryset(self):

       return amostra.objects.all()


class DetailView(generic.DetailView):
    model = amostra
    template_name = 'sedimentos/detail.html'


class amostraCreate(CreateView):
    model = amostra
    fields = ['codigo','coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem']



class amostraUpdate(UpdateView ):
     model = amostra
     fields = ['codigo', 'coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem']


class amostraDelete(DeleteView):
    model=amostra
    sucess_url=reverse_lazy('sedimentos:index')

########################################################################################################################

class IndexView2(generic.ListView):
    template_name = 'sedimentos/index2.html'
    context_object_name = 'all_continentes'

    def get_queryset(self):

       return continente.objects.all()


class DetailView2(generic.DetailView):
    model = continente
    template_name = 'sedimentos/detail.html'


class continenteCreate(CreateView):
    model = continente
    fields = ['amostra','nome','sigla']



class continenteUpdate(UpdateView ):
     model = continente
     fields = ['amostra','nome','sigla']


class continenteDelete(DeleteView):
    model=continente
    sucess_url=reverse_lazy('sedimentos:index2')
########################################################################################################################
class IndexView3(generic.ListView):
    template_name = 'sedimentos/index3.html'
    context_object_name = 'all_cidades'

    def get_queryset(self):

       return cidade.objects.all()


class DetailView3(generic.DetailView):
    model = cidade
    template_name = 'sedimentos/detail.html'


class cidadeCreate(CreateView):
    model = cidade
    fields = ['amostra','continente','país','estado','nome','geologia']



class cidadeUpdate(UpdateView ):
     model = cidade
     fields = ['amostra','continente','país','estado','nome','geologia']


class cidadeDelete(DeleteView):
    model=cidade
    sucess_url=reverse_lazy('sedimentos:index3')



########################################################################################################################

class IndexView4(generic.ListView):
    template_name = 'sedimentos/index4.html'
    context_object_name = 'all_estados'

    def get_queryset(self):

       return estado.objects.all()


class DetailView4(generic.DetailView):
    model = estado
    template_name = 'sedimentos/detail.html'


class estadoCreate(CreateView):
    model = estado
    fields = ['amostra','continente','país','nome']



class estadoUpdate(UpdateView ):
     model = estado
     fields = ['amostra','continente','país','nome']


class estadoDelete(DeleteView):
    model=estado
    sucess_url=reverse_lazy('sedimentos:index4')
########################################################################################################################

class IndexView5(generic.ListView):
    template_name = 'sedimentos/index5.html'
    context_object_name = 'all_paíss'

    def get_queryset(self):

       return país.objects.all()


class DetailView5(generic.DetailView):
    model = país
    template_name = 'sedimentos/detail.html'


class paísCreate(CreateView):
    model = país
    fields = ['amostra','continente','nome', 'região']



class paísUpdate(UpdateView ):
     model = estado
     fields = ['amostra','continente','nome', 'região']


class paísDelete(DeleteView):
    model=país
    sucess_url=reverse_lazy('sedimentos:index5')

########################################################################################################################
class IndexView6(generic.ListView):
    template_name = 'sedimentos/index6.html'
    context_object_name = 'all_ambientes'

    def get_queryset(self):

       return ambiente.objects.all()


class DetailView6(generic.DetailView):
    model = ambiente
    template_name = 'sedimentos/detail.html'


class ambienteCreate(CreateView):
    model = ambiente
    fields = ['amostra','continente','país','estado','cidade','tipo']



class ambienteUpdate(UpdateView ):
     model = ambiente
     fields = ['amostra','continente','país','estado','cidade','tipo']


class ambienteDelete(DeleteView):
    model=ambiente
    sucess_url=reverse_lazy('sedimentos:index6')

########################################################################################################################
class IndexView7(generic.ListView):
    template_name = 'sedimentos/index7.html'
    context_object_name = 'all_climas'

    def get_queryset(self):

       return clima.objects.all()


class DetailView7(generic.DetailView):
    model = ambiente
    template_name = 'sedimentos/detail.html'


class climaCreate(CreateView):
    model = ambiente
    fields = ['amostra','continente','país','estado','cidade','tipo']



class climaUpdate(UpdateView ):
     model = ambiente
     fields = ['amostra','continente','país','estado','cidade','tipo']


class climaDelete(DeleteView):
    model=ambiente
    sucess_url=reverse_lazy('sedimentos:index7')
########################################################################################################################
class UserFormView(View):
    form_class=UserForm
    template_name='sedimentos/registration_form.html'

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
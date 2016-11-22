from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import  render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import amostra
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
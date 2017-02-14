from .models import Amostra,Continente,País,Estado,Cidade,Ambiente,Clima
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms import Textarea


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name','last_name']



class ContatoForm(forms.Form):
    Nome = forms.CharField(label='Nome', max_length=100, required=True)
    Email = forms.EmailField(label=' Email', max_length=200, required=True)
    Mensagem = forms.CharField(label=' Mensagem', min_length=50, required=True, widget=forms.Textarea)




class amostraForm(forms.ModelForm):
    class Meta:
        model =Amostra
        fields = ['codigo','coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem','imagem1','imagem2','imagem3','imagem4','imagem5','imagem6','imagem7','imagem8']


class EditamostraForm(UserChangeForm):
    template_name='/something/else'
    class Meta:
        model = Amostra
        fields = ('codigo','coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem','imagem1','imagem2','imagem3','imagem4','imagem5','imagem6','imagem7','imagem8')

class continenteForm(forms.ModelForm):
    class Meta:
        model =Continente
        fields = ['amostra', 'nome', 'sigla']



class paísForm(forms.ModelForm):
    class Meta:
        model =País
        fields = ['amostra', 'continente', 'nome', 'região']



class estadoForm(forms.ModelForm):
    class Meta:
        model =Estado
        fields = ['amostra', 'continente', 'país', 'nome']



class cidadeForm(forms.ModelForm):
    class Meta:
        model =Cidade
        fields = ['amostra', 'continente', 'país', 'estado', 'nome', 'geologia']



class ambienteForm(forms.ModelForm):
    class Meta:
        model =Ambiente
        fields = ['amostra', 'continente', 'país', 'estado', 'cidade', 'tipo']




class climaForm(forms.ModelForm):
    class Meta:
        model =Clima
        fields = ['amostra', 'continente', 'país', 'estado', 'cidade', 'tipo']
from .models import Amostra,Continente,País,Estado,Cidade,Ambiente,Clima
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



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
        fields = [ 'nome']



class paísForm(forms.ModelForm):
    class Meta:
        model =País
        fields = [  'nome', 'região']



class estadoForm(forms.ModelForm):
    class Meta:
        model =Estado
        fields = [  'nome']



class cidadeForm(forms.ModelForm):
    class Meta:
        model =Cidade
        fields = [ 'nome', 'geologia']



class ambienteForm(forms.ModelForm):
    class Meta:
        model =Ambiente
        fields = [ 'tipo']



class climaForm(forms.ModelForm):
    class Meta:
        model =Clima
        fields = [ 'tipo']




class ContactForm(forms.Form):
    Nome=forms.CharField(required=True)
    Email=forms.EmailField(required=True)
    Mensagem=forms.CharField(required=True,widget=forms.Textarea)
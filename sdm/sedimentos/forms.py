from django import forms
from django.contrib.auth.models import User
from .models import amostra,continente,país,estado,cidade,ambiente,clima



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class ContatoForm(forms.Form):
    Nome = forms.CharField(label='Nome', max_length=100, required=True)
    Email = forms.EmailField(label=' Email', max_length=200, required=True)
    Mensagem = forms.CharField(label=' Mensagem', min_length=100, required=True, widget=forms.Textarea)




class amostraForm(forms.ModelForm):
    class Meta:
        model =amostra
        fields = ['codigo','coletador', 'descrição', 'tipo', 'data', 'granulometria','imagem']



class continenteForm(forms.ModelForm):
    class Meta:
        model =continente
        fields = ['amostra', 'nome', 'sigla']



class paísForm(forms.ModelForm):
    class Meta:
        model =país
        fields = ['amostra', 'continente', 'nome', 'região']



class estadoForm(forms.ModelForm):
    class Meta:
        model =estado
        fields = ['amostra', 'continente', 'país', 'nome']



class cidadeForm(forms.ModelForm):
    class Meta:
        model =cidade
        fields = ['amostra', 'continente', 'país', 'estado', 'nome', 'geologia']



class ambienteForm(forms.ModelForm):
    class Meta:
        model =ambiente
        fields = ['amostra', 'continente', 'país', 'estado', 'cidade', 'tipo']




class climaForm(forms.ModelForm):
    class Meta:
        model =clima
        fields = ['amostra', 'continente', 'país', 'estado', 'cidade', 'tipo']
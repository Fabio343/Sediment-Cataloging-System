# definição das estruturas dos campos tomando como base os models ou modelos
# cada form é para perfil, exemplares e contato
from .models import Amostra,Continente,País,Estado,Cidade,Ambiente,Clima
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    assunto=forms.CharField(max_length=50)
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem Enviada Pelo Sitema de Catalogação de Sedimentos'
        destino = 'fabio.carvalho.souza@usp.br'
        texto = """
        Assunto: %(assunto)s
        Nome: %(nome)s
        E-mail: %(email)s
        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )

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



class ContactForm(forms.Form):
    Nome = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Mensagem = forms.CharField( required=True, widget=forms.Textarea)




class amostraForm(forms.ModelForm):
    class Meta:
        model =Amostra
        fields = ['codigo','coletador','Contato', 'descrição', 'tipo', 'data', 'granulometria','imagem','imagem1','imagem2','imagem3',
                  'imagem4','imagem5','imagem6','imagem7','imagem8','Continentes','Paíss','Estados','Cidades','Ambientes','Climas']



class continenteForm(forms.ModelForm):
    class Meta:
        model =Continente
        fields = [ 'nome', 'sigla']



class paísForm(forms.ModelForm):

    class Meta:
        model =País
        fields = [ 'nome', 'região','Continentes']



class estadoForm(forms.ModelForm):
    class Meta:
        model =Estado
        fields = [ 'nome','Continentes','Paíss']



class cidadeForm(forms.ModelForm):
    class Meta:
        model =Cidade
        fields = [ 'nome', 'geologia','Continentes','Paíss','Estados']



class ambienteForm(forms.ModelForm):
    class Meta:
        model =Ambiente
        fields = [ 'tipo','Continentes','Paíss','Estados','Cidades']




class climaForm(forms.ModelForm):
    class Meta:
        model =Clima
        fields = [ 'tipo','Continentes','Paíss','Estados','Cidades']
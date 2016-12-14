from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class ContatoForm(forms.Form):
    Nome = forms.CharField(label='Nome', max_length=100, required=True)
    Email = forms.EmailField(label=' Email', max_length=200, required=True)
    Mensagem = forms.CharField(label=' Mensagem', min_length=100, required=True, widget=forms.Textarea)



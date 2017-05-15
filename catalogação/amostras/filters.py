# campo para definição dos campos da pesquisa avançada realiza a verificação da existencia de algum dado naquele campo e o exibe
from .models import Amostra,Continente,País,Estado,Cidade,Clima,Ambiente
import django_filters
from django import forms

class amostraFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='iexact')

    Continentes = django_filters.ModelMultipleChoiceFilter(queryset=Continente.objects.all(),widget=forms.CheckboxSelectMultiple)

    Data = django_filters.NumberFilter(name='data')

    Cidades = django_filters.ModelMultipleChoiceFilter(queryset=Cidade.objects.all(),widget=forms.CheckboxSelectMultiple)

    Paíss = django_filters.ModelMultipleChoiceFilter(queryset=País.objects.all(),widget=forms.CheckboxSelectMultiple)

    Estados = django_filters.ModelMultipleChoiceFilter(queryset=Estado.objects.all(),widget=forms.CheckboxSelectMultiple)

    Climas = django_filters.ModelMultipleChoiceFilter(queryset=Clima.objects.all(),widget=forms.CheckboxSelectMultiple)

    Ambientes = django_filters.ModelMultipleChoiceFilter(queryset=Ambiente.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Amostra
        fields = ['codigo', 'coletador', 'Contato', 'descrição', 'tipo', 'data','Continentes','Paíss','Estados','Cidades','Ambientes','Climas']

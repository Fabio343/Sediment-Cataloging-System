from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.db import models




# Create your models here.
class Continente(models.Model):
    nome=models.CharField(max_length=25)
    sigla=models.CharField(max_length=10)
    is_destaque=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
       return self.nome




class País(models.Model):

    nome=models.CharField(max_length=35)
    região=models.CharField(max_length=25,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Continentes = models.ManyToManyField(Continente,blank=True,)

    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
        return self.nome



class Estado(models.Model):

    nome=models.CharField(max_length=55,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Continentes = models.ManyToManyField(Continente,blank=True)
    Paíss = models.ManyToManyField(País,blank=True)


    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
         return self.nome


class Cidade(models.Model):

    nome=models.CharField(max_length=55,blank=True,null=True)
    geologia=models.TextField(max_length=300,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Continentes = models.ManyToManyField(Continente,blank=True)
    Paíss = models.ManyToManyField(País,blank=True)
    Estados = models.ManyToManyField(Estado,blank=True)

    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
        return self.nome
    def __unicode__(self):
        if self.geologia:
            return "%s, %s" % (self.nome,self.geologia)
        else:
           return "%s" % (self.nome)


class Ambiente(models.Model):
    tipo=models.CharField(max_length=30,blank=True,null=True)

    Continentes = models.ManyToManyField(Continente,blank=True)
    Paíss = models.ManyToManyField(País,blank=True)
    Estados = models.ManyToManyField(Estado,blank=True)
    Cidades = models.ManyToManyField(Cidade,blank=True)
    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
        return self.tipo


class Clima(models.Model):



    tipo=models.CharField(max_length=40,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Continentes = models.ManyToManyField(Continente,blank=True)
    Paíss = models.ManyToManyField(País,blank=True)
    Estados = models.ManyToManyField(Estado,blank=True)
    Cidades = models.ManyToManyField(Cidade,blank=True)

    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
        return self.tipo




class Amostra(models.Model):
    user = models.ForeignKey(User, default=1)
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25,blank=True,null=True)
    descrição=models.TextField(max_length=300,blank=True,null=True)
    data=models.CharField(max_length=15,blank=True,null=True)
    granulometria=models.FileField(null=True,blank=True)
    coletador=models.CharField(max_length=50,blank=True,null=True)
    Contato=models.CharField(max_length=100,blank=True,null=True)
    imagem = models.FileField(null=True,blank=True)
    imagem1 = models.FileField(null=True, blank=True)
    imagem2 = models.FileField(null=True, blank=True)
    imagem3 = models.FileField(null=True, blank=True)
    imagem4 = models.FileField(null=True, blank=True)
    imagem5 = models.FileField(null=True, blank=True)
    imagem6 = models.FileField(null=True, blank=True)
    imagem7 = models.FileField(null=True, blank=True)
    imagem8 = models.FileField(null=True, blank=True)


    Continentes = models.ManyToManyField(Continente,blank=True)
    Paíss = models.ManyToManyField(País,blank=True)
    Estados = models.ManyToManyField(Estado,blank=True)
    Cidades = models.ManyToManyField(Cidade,blank=True)
    Ambientes=models.ManyToManyField(Ambiente,blank=True)
    Climas=models.ManyToManyField(Clima,blank=True)


    def get_absolute_url(self):
        return reverse('amostras:edit')
    def __str__(self):
        return self.codigo
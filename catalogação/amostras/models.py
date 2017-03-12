from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.db import models





# Create your models here.


class Continente(models.Model):
    nome=models.CharField(max_length=25)
    is_destaque=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
       return self.nome




class País(models.Model):

    nome=models.CharField(max_length=35)
    região=models.CharField(max_length=25,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Continentes=models.ManyToManyField(Continente,through='Conti_país',blank=True)

    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome+' - '+self.região
    def __unicode__(self):
        if self.região:
            return "%s, %s" % (self.nome,self.região)
        else:
           return "%s" % (self.nome)

class Conti_país(models.Model):
    continente=models.ForeignKey(Continente,on_delete=models.CASCADE)
    país=models.ForeignKey(País,on_delete=models.CASCADE)

class Estado(models.Model):

    nome=models.CharField(max_length=55,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)
    Paíss = models.ManyToManyField(País,through='País_estado',blank=True)

    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
         return self.nome

class País_estado(models.Model):
    país = models.ForeignKey(País, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Cidade(models.Model):

    nome=models.CharField(max_length=55,blank=True,null=True)
    geologia=models.TextField(max_length=300,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Paíss = models.ManyToManyField(País ,through='País_estado_cid', blank=True)
    Estados=models.ManyToManyField(Estado ,through='País_estado_cid',blank=True)

    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome
    def __unicode__(self):
        if self.geologia:
            return "%s, %s" % (self.nome,self.geologia)
        else:
           return "%s" % (self.nome)

class País_estado_cid(models.Model):
    país = models.ForeignKey(País, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade=models.ForeignKey(Cidade,on_delete=models.CASCADE)


class Ambiente(models.Model):

    tipo=models.CharField(max_length=30,blank=True,null=True)

    Cidades=models.ManyToManyField(Cidade,through='ambi',blank=True)
    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo

class ambi(models.Model):
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ambiente=models.ForeignKey(Ambiente,on_delete=models.CASCADE)

class Clima(models.Model):

    tipo=models.CharField(max_length=40,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    Paíss = models.ManyToManyField(País,through='clim', blank=True)
    Estados = models.ManyToManyField(Estado, through='clim',blank=True)
    Cidades=models.ManyToManyField(Cidade,through='clim',blank=True)

    def get_absolute_url(self):
        return reverse('amostras:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo

class clim(models.Model):
    país = models.ForeignKey(País, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    clima=models.ForeignKey(Clima,on_delete=models.CASCADE)

class Amostra(models.Model):
    user = models.ForeignKey(User, default=1)
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=300,blank=True,null=True)
    data=models.CharField(max_length=15,blank=True,null=True)
    granulometria=models.FileField(null=True,blank=True)
    coletador=models.CharField(max_length=50,blank=True,null=True)
    imagem = models.FileField(null=True,blank=True)
    imagem1 = models.FileField(null=True, blank=True)
    imagem2 = models.FileField(null=True, blank=True)
    imagem3 = models.FileField(null=True, blank=True)
    imagem4 = models.FileField(null=True, blank=True)
    imagem5 = models.FileField(null=True, blank=True)
    imagem6 = models.FileField(null=True, blank=True)
    imagem7 = models.FileField(null=True, blank=True)
    imagem8 = models.FileField(null=True, blank=True)

    Continentes = models.ManyToManyField(Continente,through='amostr', blank=True)
    Países = models.ManyToManyField(País,through='amostr', blank=True)
    Estados = models.ManyToManyField(Estado,through='amostr', blank=True)
    Cidades = models.ManyToManyField(Cidade,through='amostr', blank=True)
    Ambientes=models.ManyToManyField(Ambiente,through='amostr',blank=True)
    Climas=models.ManyToManyField(Clima,through='amostr',blank=True)

    def get_absolute_url(self):
        return reverse('amostras:detail',kwargs={'pk': self.pk})
    def __str__(self):
        return self.codigo +' - '+self.tipo
    def __unicode__(self):
        if self.descrição:
            return "%s, %s, %s, %s, %s, %s" % (self.codigo, self.tipo,self.descrição, self.data, self.granulometria, self.coletador)
        else:
           return "%s, %s, %s, %s, %s" % (self.codigo, self.tipo, self.data, self.granulometria, self.coletador)



class amostr(models.Model):
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    país = models.ForeignKey(País, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    clima = models.ForeignKey(Clima, on_delete=models.CASCADE)
    ambiente=models.ForeignKey(Ambiente,on_delete=models.CASCADE)
    amostra=models.ForeignKey(Amostra,on_delete=models.CASCADE)
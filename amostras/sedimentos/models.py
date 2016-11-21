from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class amostra(models.Model):
    codigo=models.CharField(max_length=15)
    ambiente=models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=200)
    data=models.CharField(max_length=15)
    granulometria=models.CharField(max_length=15)
    imagem = models.CharField(max_length=1500)
    imagem2 = models.CharField(max_length=1500)
    
    def get_absolute-url(sel):
        return reverse ('sedimentos/detail', kwargs={'pk':self.pk}

    def __str__(self):
        return self.codigo +' - '+self.ambiente +' - '+self.tipo+' - '+self.data



class continente(models.Model):
    amostra=models.ForeignKey(amostra,on_delete=models.CASCADE)
    nome=models.CharField(max_length=15)
    sigla=models.CharField(max_length=15)
    is_destaque=models.BooleanField(default=False)

    def __str__(self):
       return self.nome+' - '+self.sigla



class país(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    região=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome+' - '+self.região



class estado(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    nome=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)


    def __str__(self):
         return self.nome


class cidade(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    geologia=models.TextField(max_length=255)
    graus = models.CharField(max_length=15)
    minutos = models.CharField(max_length=15)
    segundos = models.CharField(max_length=15)
    UTM = models.CharField(max_length=15)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class coletador(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    cidade= models.ForeignKey(cidade, on_delete=models.CASCADE)
    nome=models.CharField(max_length=50)
    is_destaque = models.BooleanField(default=False)


    def __str__(self):
        return self.nome


class clima(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.tipo

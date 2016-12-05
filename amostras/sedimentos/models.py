# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class amostra(models.Model):
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=300)
    data=models.CharField(max_length=15)
    granulometria=models.CharField(max_length=15)
    coletador=models.CharField(max_length=50)
    imagem = models.FileField()

    def get_absolute_url(self):
        return reverse('sedimentos:detail',kwargs={'pk': self.pk})
    def __str__(self):
        return self.codigo +' - '+self.tipo+' - '+self.data



class continente(models.Model):
    amostra=models.ForeignKey(amostra,on_delete=models.CASCADE)
    nome=models.CharField(max_length=15)
    sigla=models.CharField(max_length=15)
    is_destaque=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail2', kwargs={'pk': self.pk})
    def __str__(self):
       return self.nome+' - '+self.sigla



class país(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    região=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail3', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome+' - '+self.região



class estado(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    nome=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail4', kwargs={'pk': self.pk})
    def __str__(self):
         return self.nome


class cidade(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    geologia=models.TextField(max_length=255)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail5', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome


class ambiente(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('sedimentos:detail6', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo




class clima(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=40)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail7', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo
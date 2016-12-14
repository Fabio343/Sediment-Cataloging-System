# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class amostra(models.Model):
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=300,null=True)
    data=models.CharField(max_length=15,null=True)
    granulometria=models.CharField(max_length=15)
    coletador=models.CharField(max_length=50,null=True)
    imagem = models.FileField(null=True)

    def get_absolute_url(self):
        return reverse('sedimentos:detail',kwargs={'pk': self.pk})
    def __str__(self):
        return self.codigo +' - '+self.tipo



class continente(models.Model):
    amostra=models.ForeignKey(amostra,on_delete=models.CASCADE)
    nome=models.CharField(max_length=20,null=True)
    sigla=models.CharField(max_length=15,null=True)
    is_destaque=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:contd', kwargs={'pk': self.pk})
    def __str__(self):
       return self.nome



class país(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30,null=True)
    região=models.CharField(max_length=20,null=True)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail3', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome+' - '+self.região



class estado(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    nome=models.CharField(max_length=50,null=True)
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
    nome=models.CharField(max_length=50,null=True)
    geologia=models.TextField(max_length=300,null=True)
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
    tipo=models.CharField(max_length=30,null=True)

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
    tipo=models.CharField(max_length=40,null=True)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail7', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo
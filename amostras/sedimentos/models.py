# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class amostra(models.Model):
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=300,blank=True,null=True)
    data=models.CharField(max_length=15,blank=True,null=True)
    granulometria=models.CharField(max_length=15)
    coletador=models.CharField(max_length=50,blank=True,null=True)
    imagem = models.FileField(null=True)

    def get_absolute_url(self):
        return reverse('sedimentos:detail',kwargs={'pk': self.pk})
    def __str__(self):
        return self.codigo +' - '+self.tipo
    def __unicode__(self):
        if self.descrição:
            return "%s, %s, %s, %s, %s, %s" % (self.codigo, self.tipo,self.descrição, self.data, self.granulometria, self.coletador)
        else:
           return "%s, %s, %s, %s, %s" % (self.codigo, self.tipo, self.data, self.granulometria, self.coletador)



class continente(models.Model):
    amostra=models.ForeignKey(amostra,on_delete=models.CASCADE)
    nome=models.CharField(max_length=20)
    sigla=models.CharField(max_length=15)
    is_destaque=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:contd', kwargs={'pk': self.pk})
    def __str__(self):
       return self.nome




class país(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    região=models.CharField(max_length=20,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail3', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome+' - '+self.região
    def __unicode__(self):
        if self.região:
            return "%s, %s" % (self.nome,self.região)
        else:
           return "%s" % (self.nome)



class estado(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    nome=models.CharField(max_length=50,blank=True,null=True)
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
    nome=models.CharField(max_length=50,blank=True,null=True)
    geologia=models.TextField(max_length=300,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail5', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nome
    def __unicode__(self):
        if self.geologia:
            return "%s, %s" % (self.nome,self.geologia)
        else:
           return "%s" % (self.nome)


class ambiente(models.Model):
    amostra = models.ForeignKey(amostra, on_delete=models.CASCADE)
    continente = models.ForeignKey(continente, on_delete=models.CASCADE)
    país = models.ForeignKey(país, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30,blank=True,null=True)

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
    tipo=models.CharField(max_length=40,blank=True,null=True)
    is_destaque = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('sedimentos:detail7', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo
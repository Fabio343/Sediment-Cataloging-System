from django.db import models

# Create your models here.
class Amostra(models.Model):
    codigo=models.CharField(max_length=15)
    tipo = models.CharField(max_length=25)
    descrição=models.TextField(max_length=200)
    data=models.CharField(max_length=15)
    coletador=models.CharField(max_length=100)
    granulometria=models.CharField(max_length=15)
    imagem = models.FileField()
    imagem2 = models.FileField()

    def __str__(self):
        return self.codigo +' - '+self.tipo+' - '+self.data



class Continente(models.Model):
    Amostra=models.ForeignKey(Amostra,on_delete=models.CASCADE)
    nome=models.CharField(max_length=15)
    sigla=models.CharField(max_length=15)
    is_destaque=models.BooleanField(default=False)

    def __str__(self):
       return self.nome+' - '+self.sigla



class País(models.Model):
    Amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    Continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    região=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome+' - '+self.região



class Estado(models.Model):
    Amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    Continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    País = models.ForeignKey(País, on_delete=models.CASCADE)
    nome=models.CharField(max_length=20)
    is_destaque = models.BooleanField(default=False)


    def __str__(self):
         return self.nome


class Cidade(models.Model):
    Amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    Continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    País = models.ForeignKey(País, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    geologia=models.TextField(max_length=255)
    graus = models.CharField(max_length=15)
    minutos = models.CharField(max_length=15)
    segundos = models.CharField(max_length=15)
    UTM = models.CharField(max_length=15)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Clima(models.Model):
    Amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    Continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    País = models.ForeignKey(País, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30)
    is_destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.tipo


class Ambiente(models.Model):
    Amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    Continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    País = models.ForeignKey(País, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=25)

    def __str__(self):
        return self.tipo
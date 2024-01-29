from django.db import models


# Create your models here.

class Continentes(models.Model):
    
    nome = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to='fotos-continentes/%Y/%m/%d/', blank= True )
    legenda = models.CharField(max_length=250,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    
    
    def __str__(self):
        return(self.nome)


    
class Paises(models.Model):
    
    nome = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to="fotos-paises/%Y/%m/%d", blank=True)
    legenda = models.CharField(max_length=250,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    continente_relacionado = models.ForeignKey(Continentes, on_delete=models.CASCADE, null = False)
    popular = models.BooleanField(default=False)
    verao= models.BooleanField(default=False)
    inverno= models.BooleanField(default=False)
    outono=models.BooleanField(default=False)
    primavera=models.BooleanField(default=False)
    choque_cultural=models.BooleanField(default=False)
    historicos=models.BooleanField(default=False)
    
    def __str__(self):
        return (self.nome)

class Pontos_turisticos(models.Model):
    nome = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to='fotos_pontos-turisticos/%Y/%m/%d', blank=True)
    legenda = models.CharField(max_length=250,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    iframe_google_maps = models.TextField(default='')
    pais_relacionado = models.ForeignKey(Paises, on_delete=models.CASCADE, null= False)
    def __str__(self):
        return (self.nome)
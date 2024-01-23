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
    
    OPCOES_TOPICOS = [
        ('OS MAIS QUERIDINHOS', 'Os mais queridinhos'),
        ('PARA CURTIR O VERÃO', 'Para curtir o verão'),
        ('PARA CURTIR O INVERNO', 'Para curtir o inverno'),
    ]
    nome = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to="fotos-paises/%Y/%m/%d", blank=True)
    legenda = models.CharField(max_length=250,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    continente_relacionado = models.ForeignKey(Continentes, on_delete=models.CASCADE, null = False)
    popular = models.BooleanField(default=False)
    verao= models.BooleanField(default=False)
    inverno= models.BooleanField(default=False)
    
    def __str__(self):
        return (self.nome)

class Pontos_turisticos(models.Model):
    nome = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to='fotos_pontos-turisticos/%Y/%m/%d', blank=True)
    legenda = models.CharField(max_length=250,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    pais_relacionado = models.ForeignKey(Paises, on_delete=models.CASCADE, null= False)
    def __str__(self):
        return (self.nome)
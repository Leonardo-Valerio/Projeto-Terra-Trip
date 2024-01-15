from django.db import models

# Create your models here.

class Card(models.Model):
    nome = models.CharField(max_length=100, null=False)
    imagem = models.CharField(max_length=200)
    descricao = models.CharField(max_length=250,null=False, blank=False)
    informacao = models.TextField(null=False, blank=False)

def __str__(self):
    return(f"Card [nome={self.nome}]")
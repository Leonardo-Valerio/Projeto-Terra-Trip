from django.db import models

# Create your models here.

class Card(models.Model):
    OPCOES_CATEGORIAS = [
        ("PAÍS", "País",),
        ("CONTINENTE", "Continente"),
    ]
    nome = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    imagem = models.CharField(max_length=200)
    descricao = models.CharField(max_length=250,null=False, blank=False)
    informacao = models.TextField(null=False, blank=False),
    continente_relacionado = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,limit_choices_to={'categoria': 'CONTINENTE'})
    
    def __str__(self):
        return(self.nome)
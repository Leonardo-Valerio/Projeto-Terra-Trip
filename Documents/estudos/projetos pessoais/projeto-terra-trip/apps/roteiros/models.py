from django.db import models
from apps.home.models import Paises
from django.contrib.auth.models import User

class Roteiro(models.Model):
    ESTACOES =[
        ('verão','Verão'),
        ('inverno','Inverno'),
        ('primavera','Primavera'),
        ('outono','Outono'),
    ]
    nome= models.CharField(max_length=100, null=False)
    dias= models.IntegerField(null = False)
    epoca= models.CharField(max_length=10, choices=ESTACOES, null=False)
    usuario_roteiro = models.ForeignKey(User,on_delete=models.CASCADE)
    grupo_paises = models.JSONField(null=True, blank=True, default=list)
    roteiro_gerado = models.TextField(null = True, blank = True)

    def __str__(self):
        return (self.nome)
    
    

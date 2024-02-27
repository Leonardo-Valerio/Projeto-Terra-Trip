from django.shortcuts import render, redirect, get_object_or_404
from apps.roteiros.forms import RoteiroForms
from apps.roteiros.models import Roteiro
from apps.home.models import Paises


def roteiros(request, roteiro_id, pais_id):
    
    roteiro = get_object_or_404(Roteiro,pk=roteiro_id)
    pais = get_object_or_404(Paises,pk=pais_id)
    roteiro.grupo_paises.append(pais.nome)
    roteiro.save()
    return render(request, 'roteiros/roteiros.html', {'pais':pais, 'roteiro':roteiro})

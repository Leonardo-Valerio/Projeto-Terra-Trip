from django.shortcuts import render, redirect, get_object_or_404
from apps.roteiros.forms import RoteiroForms
from apps.roteiros.models import Roteiro
from apps.home.models import Paises



def roteiros(request, roteiro_id, pais_id):
    
    roteiro = get_object_or_404(Roteiro,pk=roteiro_id)
    pais = get_object_or_404(Paises,pk=pais_id)
    for item in roteiro.grupo_paises:
        if item["nome"] == pais.nome:
            return redirect('home') 
       
    roteiro.grupo_paises.append({"nome":pais.nome,"imagem":pais.imagem.url})

    
    roteiro.save()
    return render(request, 'roteiros/roteiros.html', {'pais':pais, 'roteiro':roteiro})

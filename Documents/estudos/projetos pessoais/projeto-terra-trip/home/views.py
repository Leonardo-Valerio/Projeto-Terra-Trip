from django.shortcuts import render, get_object_or_404
from home.models import Continentes,Paises, Pontos_turisticos, Cidades

dados_continente = Continentes.objects.all()


def index(request):
    return render(request, 'home/index.html', {'dados':dados_continente})

def continente(request, img_id):
    card_continente = get_object_or_404(Continentes, pk=img_id)
    dados_paises_populares = Paises.objects.filter(continente_relacionado=card_continente,popular=True)
    dados_paises_historicos= Paises.objects.filter(continente_relacionado=card_continente,historicos=True)
    dados_paises_choque_cultural= Paises.objects.filter(continente_relacionado=card_continente,choque_cultural=True)
    dados_paises_verao= Paises.objects.filter(continente_relacionado=card_continente,verao=True)
    dados_paises_inverno=Paises.objects.filter(continente_relacionado=card_continente,inverno=True)
    dados_paises_primavera=Paises.objects.filter(continente_relacionado=card_continente,primavera=True)
    dados_paises_outono=Paises.objects.filter(continente_relacionado=card_continente,outono=True)
    return render(request, 'home/continente.html', {
        'dados_paises_populares':dados_paises_populares,
        "card": card_continente,
        'dados_paises_historicos': dados_paises_historicos, 
        'dados_paises_choque_cultural':dados_paises_choque_cultural,
        'dados_paises_verao': dados_paises_verao,
        'dados_paises_inverno': dados_paises_inverno,
        'dados_paises_primavera': dados_paises_primavera,
        'dados_paises_outono': dados_paises_outono
        })

def pais(request, pais_id):
    item_pais = get_object_or_404(Paises,pk=pais_id)
    dados_cidades = Cidades.objects.filter(pais_relacionado=item_pais)
    dados_pontos_turisticos = Pontos_turisticos.objects.filter(cidade_relacionada__in=dados_cidades)
    return render(request,'home/pais.html', {'item_pais':item_pais ,'dados_cidades':dados_cidades , 'dados_pontos_turisticos':dados_pontos_turisticos})

def sobre_nos(request):
    return render(request, 'home/sobre_nos.html')
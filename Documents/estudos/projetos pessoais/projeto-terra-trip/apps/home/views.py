from django.shortcuts import render, get_object_or_404,redirect
from apps.home.models import Continentes,Paises, Pontos_turisticos, Cidades
from django.contrib import messages
from django.shortcuts import render, redirect
from apps.roteiros.forms import RoteiroForms
from apps.roteiros.models import Roteiro,Viagem


dados_continente = Continentes.objects.all()


def index(request):
    dados_paises_populares_home = Paises.objects.filter(popular=True, presente_na_home=True)
    dados_paises_historicos_home= Paises.objects.filter(presente_na_home=True, historicos=True)
    dados_paises_choque_cultural_home= Paises.objects.filter(presente_na_home=True, choque_cultural=True)
    dados_paises_verao_home= Paises.objects.filter(presente_na_home=True, verao=True)
    dados_paises_inverno_home=Paises.objects.filter(presente_na_home=True, inverno=True)
    dados_paises_primavera_home=Paises.objects.filter(presente_na_home=True, primavera=True)
    dados_paises_outono_home=Paises.objects.filter(presente_na_home=True, outono=True)
    return render(request, 'home/index.html', {
        'dados':dados_continente,
        'dados_paises_populares_home': dados_paises_populares_home,    
        'dados_paises_historicos_home':dados_paises_historicos_home,
        'dados_paises_choque_cultural_home':dados_paises_choque_cultural_home,
        'dados_paises_verao_home':dados_paises_verao_home,
        'dados_paises_inverno_home':dados_paises_inverno_home,
        'dados_paises_primavera_home':dados_paises_primavera_home,
        'dados_paises_outono_home':dados_paises_outono_home                                   
        })

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
    if not request.user.is_authenticated:
        messages.error(request,"Para acessar essa página é necessário você fazer seu login")
        return redirect('login')
    item_pais = get_object_or_404(Paises,pk=pais_id)
    dados_cidades = Cidades.objects.filter(pais_relacionado=item_pais)
    dados_pontos_turisticos = Pontos_turisticos.objects.filter(cidade_relacionada__in=dados_cidades)
    form_roteiro = RoteiroForms()
    if request.method == 'POST':
        form_roteiro = RoteiroForms(request.POST)
        if form_roteiro.is_valid():
            roteiro = form_roteiro.save(commit=False)
            roteiro.usuario_roteiro = request.user
            roteiro.save()
    roteiros = Roteiro.objects.filter(usuario_roteiro=request.user)
    return render(request,'home/pais.html', {'item_pais':item_pais ,'dados_cidades':dados_cidades , 'dados_pontos_turisticos':dados_pontos_turisticos, 'form_roteiro': form_roteiro, "roteiros":roteiros})

def sobre_nos(request):
    return render(request, 'home/sobre_nos.html')


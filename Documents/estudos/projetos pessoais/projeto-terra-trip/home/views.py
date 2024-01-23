from django.shortcuts import render, get_object_or_404
from home.models import Continentes,Paises

dados_continente = Continentes.objects.all()


def index(request):
    return render(request, 'home/index.html', {'dados':dados_continente})

def continente(request, img_id):
    card_continente = get_object_or_404(Continentes, pk=img_id)
    dados_pais = Paises.objects.filter(continente_relacionado=card_continente)
    return render(request, 'home/continente.html', {'dados':dados_pais, "card": card_continente})

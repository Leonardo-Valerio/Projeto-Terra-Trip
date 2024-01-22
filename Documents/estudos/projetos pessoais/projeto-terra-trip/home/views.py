from django.shortcuts import render, get_object_or_404
from home.models import Card

dados_continente = Card.objects.filter(categoria='CONTINENTE')


def index(request):
    return render(request, 'home/index.html', {'dados':dados_continente})

def continente(request, img_id):
    card_continente = get_object_or_404(Card, pk=img_id)
    dados_pais = Card.objects.filter(categoria= 'PAÍS', continente_relacionado=card_continente)
    return render(request, 'home/continente.html', {'dados':dados_pais, "card": card_continente})

from django.shortcuts import render, get_object_or_404
from home.models import Card

dados = Card.objects.all()

def index(request):
    return render(request, 'home/index.html', {'dados':dados})

def continente(request, img_id):
    card = get_object_or_404(Card, pk=img_id)
    return render(request, 'home/continente.html', {'dados':dados, "card": card})

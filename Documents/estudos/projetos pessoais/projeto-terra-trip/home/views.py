from django.shortcuts import render
from home.models import Card

dados = Card.objects.all()

def index(request):
    return render(request, 'home/index.html', {'dados':dados})

def continente(request):
    return render(request, 'home/continente.html', {'dados':dados})

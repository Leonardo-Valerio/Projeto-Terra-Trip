from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def continente(request):
    return render(request, 'home/continente.html')

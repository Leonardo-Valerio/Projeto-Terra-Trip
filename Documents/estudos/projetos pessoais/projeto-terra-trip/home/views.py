from django.shortcuts import render

dados = {
    1:{
        'nome': 'Europa',
        'img':''
    },
    2:{
        'nome': 'América',
        'img':''
    }
}

def index(request):
    return render(request, 'home/index.html', {'card':dados})

def continente(request):
    return render(request, 'home/continente.html')

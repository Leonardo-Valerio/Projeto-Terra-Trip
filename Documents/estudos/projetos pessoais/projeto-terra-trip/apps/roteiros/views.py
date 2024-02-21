from django.shortcuts import render

def roteiros(request):
    return render(request, 'roteiros/roteiros.html')

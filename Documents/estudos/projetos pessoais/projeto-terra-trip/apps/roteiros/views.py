from django.shortcuts import render, redirect
from apps.roteiros.forms import RoteiroForms


def roteiros(request):
    
    
    return render(request, 'roteiros/roteiros.html')

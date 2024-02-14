from django.shortcuts import render
from usuarios.forms import LoginForm, CadastroForm

def login(request):
    forms = LoginForm()
    return render(request, 'usuarios/login.html', {"forms":forms})

def cadastro(request):
    forms = CadastroForm
    return render(request, 'usuarios/cadastro.html', {"forms":forms})
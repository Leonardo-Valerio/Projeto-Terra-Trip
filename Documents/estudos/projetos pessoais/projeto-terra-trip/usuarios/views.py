from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth,messages

def login(request):
    forms = LoginForm()

    if request.method == "POST":
        forms=LoginForm(request.POST)
        if forms.is_valid:
            nome = forms["username"].value()
            senha = forms["senha"].value()
            usuario = auth.authenticate(request,username=nome,password=senha)
            if usuario != None:
                messages.success(request,f"Login realizado com sucesso! Olá {nome}")
                auth.login(request, usuario)
                return redirect ('home')
            else:
                messages.error(request,"Erro ao efetuar login")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"forms":forms})

def cadastro(request):
    forms = CadastroForm()

    if request.method == "POST":
        forms = CadastroForm(request.POST)
        if forms.is_valid:
            nome = forms["novo_nome"].value()
            senha1 = forms["nova_senha"].value()
            senha2 = forms["confirmar_senha"].value()
            email = forms["email"].value()
            if senha1!= senha2:
               messages.error(request,"As senhas não são iguais")
               return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,"Nome já existente")
            return redirect('cadastro')
        usuario = User.objects.create_user(
            username=nome,
            password= senha1,
            email=email
        )
        usuario.save()
        messages.success(request,f"Cadastro efetuado com sucesso! Que bom ter você conosco, {nome}! ")
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"forms":forms})

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout realizado com sucesso")
    return redirect('login')

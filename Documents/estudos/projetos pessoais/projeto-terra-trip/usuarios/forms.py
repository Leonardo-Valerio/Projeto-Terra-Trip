from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite o nome de login"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForm(forms.Form):
    novo_nome = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Digite o nome para login"
            }
        )
    )
    nova_senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Crie sua senha"
            }
        )
    )
    confirmar_senha = forms.CharField(
        label="Confirmar senha",
        required=True,
        max_length=70,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme aqui a sua senha"
            }
        )
    )
    email = forms.CharField(
        label="E-mail",
        required=True,
        max_length=200,
        min_length=5,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex: abcd@gmail.com"
                
            }
        )
    )

  
          
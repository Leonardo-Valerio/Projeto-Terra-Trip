from django import forms
from apps.roteiros.models import Roteiro


class RoteiroForms(forms.ModelForm):
    class Meta:
        model=Roteiro
        exclude=['usuario_roteiro','grupo_paises',]
        labels={
            "nome":"Nome",
            "dias":"Dias",
            "epoca":"Época"
        }
        
        widgets={
            "nome": forms.TextInput(attrs={'class':'input-roteiro'}),
            "dias": forms.NumberInput(attrs={'class':'input-roteiro'}),
            "epoca": forms.Select(attrs={'class':'input-roteiro'}),
        }
from django.contrib import admin
from apps.roteiros.models import Roteiro,Viagem

class listandoRoteiros(admin.ModelAdmin):
    list_display=('id', 'nome', 'usuario_roteiro')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoViagem(admin.ModelAdmin):
    list_display=('id','nome_pais','identificador_pais')
    list_display_links=('id','nome_pais','identificador_pais')
    search_fields=('nome_pais',)
# Register your models here.
    
admin.site.register(Roteiro,listandoRoteiros)
admin.site.register(Viagem,listandoViagem)
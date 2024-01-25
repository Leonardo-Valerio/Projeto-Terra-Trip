from django.contrib import admin
from home.models import Continentes, Paises, Pontos_turisticos


class listandoCardsContinentes(admin.ModelAdmin):
    list_display=('id', 'nome')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoCardsPais(admin.ModelAdmin):
    list_display=('id','nome', 'continente_relacionado')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoCardsPontos(admin.ModelAdmin):
    list_display=('id','nome', 'pais_relacionado')
    list_display_links=('id', 'nome')
    search_fields=('nome',)
    
admin.site.register(Continentes, listandoCardsContinentes)
admin.site.register(Paises, listandoCardsPais)
admin.site.register(Pontos_turisticos, listandoCardsPontos)



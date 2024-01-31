from django.contrib import admin
from home.models import Continentes, Paises, Pontos_turisticos, Cidades


class listandoCardsContinentes(admin.ModelAdmin):
    list_display=('id', 'nome')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoCardsPais(admin.ModelAdmin):
    list_display=('id','nome', 'continente_relacionado')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoCidades(admin.ModelAdmin):
    list_display=('id','nome', 'pais_relacionado')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoPontos(admin.ModelAdmin):
    list_display=('id','nome','cidade_relacionada' )
    list_display_links=('id', 'nome')
    search_fields=('nome',)
    
admin.site.register(Continentes, listandoCardsContinentes)
admin.site.register(Paises, listandoCardsPais)
admin.site.register(Cidades, listandoCidades)
admin.site.register(Pontos_turisticos, listandoPontos)



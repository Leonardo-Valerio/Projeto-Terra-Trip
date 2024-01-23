from django.contrib import admin
from home.models import Continentes, Paises, Pontos_turisticos


class listandoCards(admin.ModelAdmin):
    list_display=('id', 'nome')
    list_display_links=('id', 'nome')
    search_fields=('nome',)
    
admin.site.register(Continentes, listandoCards)
admin.site.register(Paises, listandoCards)
admin.site.register(Pontos_turisticos, listandoCards)



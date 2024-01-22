from django.contrib import admin
from home.models import Card


class listandoCards(admin.ModelAdmin):
    list_display=('id', 'nome', 'categoria', 'continente_relacionado')
    list_display_links=('id', 'nome')
    search_fields=('nome',)
    list_filter =('categoria',)
admin.site.register(Card,listandoCards)

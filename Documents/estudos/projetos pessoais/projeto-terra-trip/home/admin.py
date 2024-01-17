from django.contrib import admin
from home.models import Card

class listandoCards(admin.ModelAdmin):
    list_display=('id', 'nome')
    list_display_links=('id', 'nome')
admin.site.register(Card,listandoCards)

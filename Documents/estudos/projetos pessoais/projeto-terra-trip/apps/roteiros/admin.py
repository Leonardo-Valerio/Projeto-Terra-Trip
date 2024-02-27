from django.contrib import admin
from apps.roteiros.models import Roteiro

class listandoRoteiros(admin.ModelAdmin):
    list_display=('id', 'nome', 'usuario_roteiro')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

class listandoViagem(admin.ModelAdmin):
    list_display=('id','identificador_roteiro','identificador_pais')
    list_display_links=('id','identificador_roteiro','identificador_pais')
    search_fields=('identificador_pais',)
# Register your models here.
    
admin.site.register(Roteiro,listandoRoteiros)

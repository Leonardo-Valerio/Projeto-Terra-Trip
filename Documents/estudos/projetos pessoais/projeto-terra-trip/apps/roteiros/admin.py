from django.contrib import admin
from apps.roteiros.models import Roteiro

class listandoRoteiros(admin.ModelAdmin):
    list_display=('id', 'nome', 'usuario_roteiro')
    list_display_links=('id', 'nome')
    search_fields=('nome',)

# Register your models here.
    
admin.site.register(Roteiro,listandoRoteiros)

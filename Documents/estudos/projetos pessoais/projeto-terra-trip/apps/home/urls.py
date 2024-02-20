from django.urls import path
from apps.home.views import index, continente, pais, sobre_nos

urlpatterns = [
    path('', index, name='home'),
    path('continente/<int:img_id>',continente, name='continente'),
    path('pais/<int:pais_id>',pais,name='pais'),
    path('sobre_nos',sobre_nos, name='sobre_nos')
]

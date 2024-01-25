from django.urls import path
from home.views import index, continente, pais

urlpatterns = [
    path('', index, name='home'),
    path('continente/<int:img_id>',continente, name='continente'),
    path('pais/<int:pais_id>',pais,name='pais'),
]

from django.urls import path
from apps.roteiros.views import roteiros,todos_os_roteiros,editar_roteiro

urlpatterns = [
    path('roteiros/<int:roteiro_id>/', roteiros, name='roteiros'),
    path('roteiros/<int:pais_id>/<int:roteiro_id>', roteiros, name='roteiros_com_pais'),
    path('roteiros/todos-roteiros/', todos_os_roteiros, name='todos_roteiros'),
    path('roteiros/editar_roteiro/<int:roteiro_id>',editar_roteiro, name='editar_roteiro' )
    
]
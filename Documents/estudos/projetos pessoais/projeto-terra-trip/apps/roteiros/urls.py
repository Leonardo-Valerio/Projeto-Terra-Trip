from django.urls import path
from apps.roteiros.views import roteiros,todos_os_roteiros

urlpatterns = [
    path('roteiros/<int:roteiro_id>/', roteiros, name='roteiros'),
    path('roteiros/<int:pais_id>/<int:roteiro_id>', roteiros, name='roteiros_com_pais'),
    path('roteiros/todos-roteiros/', todos_os_roteiros, name='todos_roteiros'),
    
    
    
]
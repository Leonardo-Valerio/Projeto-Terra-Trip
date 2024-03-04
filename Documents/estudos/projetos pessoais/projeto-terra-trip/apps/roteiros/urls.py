from django.urls import path
from apps.roteiros.views import roteiros

urlpatterns = [
    path('roteiros/<int:pais_id>/<int:roteiro_id>', roteiros, name='roteiros'),
    
]
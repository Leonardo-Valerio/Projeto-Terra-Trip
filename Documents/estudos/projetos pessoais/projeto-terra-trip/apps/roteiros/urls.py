from django.urls import path
from apps.roteiros.views import roteiros

urlpatterns = [
    path('roteiros/', roteiros, name='roteiros')
]
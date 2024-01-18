from django.urls import path
from home.views import index, continente

urlpatterns = [
    path('', index, name='home'),
    path('continente/<int:img_id>',continente, name='continente'),
]

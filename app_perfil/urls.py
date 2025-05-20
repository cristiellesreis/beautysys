from django.urls import path
from .views import perfil_view, seguranca

urlpatterns = [
    path('', perfil_view, name='perfil'),
    path('seguranca', seguranca, name='seguranca'),
]
from django.urls import path
from .views import perfil_view

urlpatterns = [
    path('', perfil_view, name='perfil'),
]
from django.urls import path
from app_perfil.views import *

urlpatterns = [
    path('', perfil, name='perfil')
]

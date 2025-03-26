from django.urls import path
from app_agendamento.views import *

urlpatterns = [
    path('', agendamento, name='agendamento')
]

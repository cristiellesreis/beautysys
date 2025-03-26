from django.urls import path
from app_financas.views import *

urlpatterns = [
    path('', financas, name='financas')
]

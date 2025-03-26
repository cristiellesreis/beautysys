from django.urls import path
from app_estoque.views import *

urlpatterns = [
    path('', estoque, name='estoque')
]

from django.urls import path
from app_estoque.views import estoque, adicionar_item_estoque, remove_item_estoque

urlpatterns = [
    path('', estoque, name='estoque'),
    path('estoque/adicionar/', adicionar_item_estoque, name='adicionar_item_estoque'),
    path('estoque/remover/<int:pk>/', remove_item_estoque, name='remove_item_estoque'),
]

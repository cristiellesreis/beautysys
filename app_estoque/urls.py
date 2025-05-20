from django.urls import path
from app_estoque.views import estoque, cadastrar_item_estoque, remover_item_estoque, editar_item_estoque, \
    obter_item_estoque

urlpatterns = [
    path('', estoque, name='estoque'),
    path('cadastrar/', cadastrar_item_estoque, name='cadastrar_item_estoque'),
    path('remover/<int:id_item_estoque>/', remover_item_estoque, name='remover_item_estoque'),
    path('editar/<int:id_item_estoque>/', editar_item_estoque, name='editar_item_estoque'),
    path('obter/<int:id_item_estoque>/', obter_item_estoque, name='obter_item_estoque'),
]

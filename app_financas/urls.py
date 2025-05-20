from django.urls import path
from . import views
from .views import financas

urlpatterns = [
    path('', financas, name='financas'),
    path('grafico-dados-mensal/', views.grafico_receitas_despesas_mensal, name='grafico_dados_mensal'),
    path('receitas/', views.listar_receitas, name='listar_receitas'),
    path('receitas/cadastrar/', views.cadastrar_receita, name='cadastrar_receita'),
    path('receitas/remover/<int:id_receita>/', views.remover_receita, name='remover_receita'),
    path('receitas/editar/<int:id_receita>/', views.editar_receita, name='editar_receita'),
    path('receitas/obter/<int:id_receita>/', views.obter_receita, name='obter_receita'),
    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/cadastrar/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesas/remover/<int:id_despesa>/', views.remover_despesa, name='remover_despesa'),
    path('despesas/editar/<int:id_despesa>/', views.editar_despesa, name='editar_despesa'),
    path('despesas/obter/<int:id_despesa>/', views.obter_despesa, name='obter_despesa'),
]

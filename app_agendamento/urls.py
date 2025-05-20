from django.urls import path

from app_agendamento import views

urlpatterns = [
    path('', views.agendamento, name='agendamento'),
    path('cadastrar/', views.cadastrar_agendamento, name='cadastrar_agendamento'),
    path('remover/<int:id_agendamento>/', views.remover_agendamento, name='remover_agendamento'),
    path('editar/<int:id_agendamento>/', views.editar_agendamento, name='editar_agendamento'),
    path('obter/<int:id_agendamento>/', views.obter_agendamento, name='obter_agendamento'),
    path('clientes/', views.listar_clientes, name='lista_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/remover/<int:id_cliente>/', views.remover_cliente, name='remover_cliente'),
    path('clientes/editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/obter/<int:id_cliente>/', views.obter_cliente, name='obter_cliente'),
]

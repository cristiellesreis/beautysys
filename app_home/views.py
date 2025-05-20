from app_estoque.models import ItemEstoque
from app_agendamento.models import Cliente, Agendamento
from app_financas.models import Receita, Despesa
from app_perfil.models import Perfil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from django.utils import timezone
import json


def landing_page(request):
    return render(request, 'landing_page/landing_page.html')


@login_required
def home(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    total_clientes = Cliente.objects.filter(perfil=perfil).count()
    total_estoque = ItemEstoque.objects.filter(perfil=perfil).aggregate(total=Sum('quantidade'))['total'] or 0

    hoje = timezone.localtime().date()
    total_hoje = Agendamento.objects.filter(cliente__perfil=perfil, data_hora_inicio__date=hoje).count()
    agendamentos_hoje = Agendamento.objects.filter(cliente__perfil=perfil, data_hora_inicio__date=hoje)

    inicio_semana = hoje - timezone.timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timezone.timedelta(days=6)

    agendamentos_semana = Agendamento.objects.filter(
        cliente__perfil=perfil,
        data_hora_inicio__date__range=(inicio_semana, fim_semana)
    ).order_by('data_hora_inicio')

    mes_atual = hoje.month
    ano_atual = hoje.year

    total_receita_mes = Receita.objects.filter(
        perfil=perfil,
        data__year=ano_atual,
        data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    total_despesa_mes = Despesa.objects.filter(
        perfil=perfil,
        data__year=ano_atual,
        data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    margem_lucro = total_receita_mes - total_despesa_mes

    status_counts = Agendamento.objects.filter(cliente__perfil=perfil).values('status').annotate(total=Count('status'))
    status_dict = {item['status']: item['total'] for item in status_counts}

    status_agendado = status_dict.get('agendado', 0)
    status_cancelado = status_dict.get('cancelado', 0)
    status_concluido = status_dict.get('concluido', 0)

    dados_receita_categoria = Receita.objects.filter(perfil=perfil) \
        .values('categoria') \
        .annotate(total=Sum('valor')) \
        .order_by('-total')

    dados_despesa_categoria = Despesa.objects.filter(perfil=perfil) \
        .values('categoria') \
        .annotate(total=Sum('valor')) \
        .order_by('-total')

    lista_receitas = [
        {'categoria': str(r['categoria']), 'total': float(r['total']) or 0} 
        for r in dados_receita_categoria
    ]
    lista_despesas = [
        {'categoria': str(d['categoria']), 'total': float(d['total']) or 0} 
        for d in dados_despesa_categoria
    ]

    dados_receita = json.dumps(lista_receitas)
    dados_despesa = json.dumps(lista_despesas)

    return render(request, 'dashboard/dashboard.html', {
        'total_clientes': total_clientes,
        'total_estoque': total_estoque,
        'total_hoje': total_hoje,
        'margem_lucro': margem_lucro,
        'agendamentos_hoje': agendamentos_hoje,
        'agendamentos_semana': agendamentos_semana,
        'status_agendado': status_agendado,
        'status_cancelado': status_cancelado,
        'status_concluido': status_concluido,
        'dados_receita_categoria': lista_receitas,
        'dados_despesa_categoria': lista_despesas,
        'dados_receita': dados_receita,
        'dados_despesa': dados_despesa,
    })

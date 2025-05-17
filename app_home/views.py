from app_estoque.models import Item_Estoque
from app_agendamento.models import Cliente, Agendamento
from app_financas.models import Receita, Despesa
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum, Count
from django.utils import timezone



def landing_page(request):
    return render(request, 'landing_page/landing_page.html')

@login_required
def home(request):
    total_clientes = Cliente.objects.count()
    total_estoque = Item_Estoque.objects.aggregate(total=Sum('quantidade'))['total'] or 0

    hoje = timezone.localtime().date()
    total_hoje = Agendamento.objects.filter(data_hora_inicio__date=hoje).count()
    agendamentos_hoje = Agendamento.objects.filter(data_hora_inicio__date=hoje)

    inicio_semana = hoje - timezone.timedelta(days=hoje.weekday())  
    fim_semana = inicio_semana + timezone.timedelta(days=6)         

    agendamentos_semana = Agendamento.objects.filter(
    data_hora_inicio__date__range=(inicio_semana, fim_semana)
    ).order_by('data_hora_inicio')

    mes_atual = hoje.month
    ano_atual = hoje.year

    total_receita_mes = Receita.objects.filter(
        data__year=ano_atual, data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    total_despesa_mes = Despesa.objects.filter(
        data__year=ano_atual, data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    margem_lucro = total_receita_mes - total_despesa_mes

    status_counts = Agendamento.objects.values('status').annotate(total=Count('status'))
    status_dict = {item['status']: item['total'] for item in status_counts}

    status_agendado = status_dict.get('agendado', 0)
    status_cancelado = status_dict.get('cancelado', 0)
    status_concluido = status_dict.get('concluido', 0)


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
    })

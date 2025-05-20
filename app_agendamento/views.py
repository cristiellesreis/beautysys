from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from utils.sns_sms import enviar_sms
from app_agendamento.forms import ClienteForm, AgendamentoForm
from app_agendamento.models import Cliente, Agendamento
from app_perfil.models import Perfil

@login_required
def agendamento(request):
    perfil = get_perfil(request)
    agendamentos = Agendamento.objects.filter(
        cliente__perfil=perfil
    ).order_by('-data_hora_inicio')

    todos_clientes = Cliente.objects.filter(
        perfil=perfil
    ).order_by('nome')

    hoje = timezone.localtime().date()
    total_hoje = Agendamento.objects.filter(
        data_hora_inicio__date=hoje,
        cliente__perfil=perfil
    ).count()

    ontem = hoje - timezone.timedelta(days=1)
    total_ontem = Agendamento.objects.filter(
        data_hora_inicio__date=ontem,
        cliente__perfil=perfil
    ).count()

    diferenca = total_hoje - total_ontem

    return render(request, 'agenda/agenda.html', {
        'agendamentos': agendamentos,
        'todos_clientes': todos_clientes,
        'total_hoje': total_hoje,
        'diferenca': diferenca
    })


@login_required
def cadastrar_agendamento(request):
    perfil = get_perfil(request)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)

            if agendamento.cliente.perfil != perfil:
                messages.error(request, 'Cliente inválido para seu perfil.')
                return redirect('agendamento')

            agendamento.save()

            if agendamento.lembrete_sms:
                processar_lembrete_sms(agendamento, request)

            query_params = request.GET.urlencode()
            url = reverse('agendamento')
            if query_params:
                url += f'?{query_params}'

            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect(url)

    else:
        form = AgendamentoForm()

    form.fields['cliente'].queryset = Cliente.objects.filter(perfil=perfil)
    return render(request, 'agenda/agenda.html', {'form': form})

@login_required
def obter_agendamento(request, id_agendamento):
    perfil = get_perfil(request)

    agendamento_consultado = get_object_or_404(
        Agendamento,
        id=id_agendamento,
        cliente__perfil=perfil
    )

    dados = {
        'id': agendamento_consultado.id,
        'cliente': {
            'id': agendamento_consultado.cliente.id,
            'nome': agendamento_consultado.cliente.nome,
            'telefone': agendamento_consultado.cliente.telefone
        },
        'servico': agendamento_consultado.servico,
        'data_hora_inicio': agendamento_consultado.data_hora_inicio.strftime('%Y-%m-%dT%H:%M:%S'),
        'data_hora_fim': agendamento_consultado.data_hora_fim.strftime('%Y-%m-%dT%H:%M:%S'),
        'observacoes': agendamento_consultado.observacoes or '',
        'status': agendamento_consultado.status,
        'status_display': agendamento_consultado.get_status_display(),
    }

    return JsonResponse(dados)


@login_required
def editar_agendamento(request, id_agendamento):
    perfil = get_perfil(request)

    agendamento_consultado = get_object_or_404(
        Agendamento,
        id=id_agendamento,
        cliente__perfil=perfil
    )

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento_consultado)

        if form.is_valid():
            agendamento = form.save(commit=False)

            if agendamento.cliente.perfil != perfil:
                messages.error(request, 'Cliente inválido para seu perfil.')
                return redirect('agendamento')

            agendamento.save()

            if agendamento.lembrete_sms:
                processar_lembrete_sms(agendamento, request)

            query_params = request.GET.urlencode()
            url = reverse('agendamento')
            if query_params:
                url += f'?{query_params}'

            messages.success(request, 'Agendamento alterado com sucesso!')
            return redirect(url)

    else:
        form = AgendamentoForm(instance=agendamento_consultado)
        form.fields['cliente'].queryset = Cliente.objects.filter(perfil=perfil)

    return render(request, 'agenda/editar_agendamento.html', {'form': form})


@login_required
def remover_agendamento(request, id_agendamento):
    perfil = get_perfil(request)

    agendamento_consultado = get_object_or_404(
        Agendamento,
        id=id_agendamento,
        cliente__perfil=perfil
    )

    if request.method == 'POST':
        agendamento_consultado.delete()
        messages.success(request, 'Agendamento removido com sucesso!')
        return redirect('agendamento')

    messages.error(request, 'Método inválido para remoção.')
    return redirect('agendamento')


@login_required
def cadastrar_cliente(request):
    perfil = get_perfil(request)

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.perfil = perfil
            cliente.save()

            query_params = request.GET.urlencode()
            url = reverse('lista_clientes')
            if query_params:
                url += f'?{query_params}'

            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect(url)
    else:
        form = ClienteForm()

    return render(request, 'agenda/listar_clientes.html', {'form': form})


@login_required
def listar_clientes(request):
    perfil = get_perfil(request)
    termo = request.GET.get('criterio', '')

    if termo:
        clientes = Cliente.objects.filter(perfil=perfil, nome__icontains=termo).order_by('-data_cadastro')
    else:
        clientes = Cliente.objects.filter(perfil=perfil).order_by('-data_cadastro')

    return render(request, 'agenda/listar_clientes.html', {
        'clientes': clientes,
        'termo': termo
    })


@login_required
def obter_cliente(request, id_cliente):
    perfil = get_perfil(request)

    cliente = get_object_or_404(Cliente, id=id_cliente, perfil=perfil)

    dados = {
        'id': cliente.id,
        'nome': cliente.nome,
        'telefone': cliente.telefone,
        'email': cliente.email or '',
        'data_cadastro': cliente.data_cadastro.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return JsonResponse(dados)


@login_required
def editar_cliente(request, id_cliente):
    perfil = get_perfil(request)

    cliente = get_object_or_404(Cliente, id=id_cliente, perfil=perfil)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('lista_clientes')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Cliente alterado com sucesso!')
            return redirect(url)

    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'agenda/editar_cliente.html', {'form': form})


@login_required
def remover_cliente(request, id_cliente):
    perfil = get_perfil(request)

    cliente = get_object_or_404(Cliente, id=id_cliente, perfil=perfil)

    try:
        cliente.delete()
        messages.success(request, 'Cliente removido com sucesso!')
    except ProtectedError:
        messages.error(
            request,
            'Não é possível remover o cliente pois existem agendamentos vinculados. '
            'Delete ou altere os agendamentos primeiro.'
        )

    query_params = request.GET.urlencode()
    url = reverse('lista_clientes')

    if query_params:
        url += f'?{query_params}'

    return redirect(url)


def get_perfil(request):
    return get_object_or_404(Perfil, user=request.user)


def processar_lembrete_sms(agendamento, request):
    perfil = request.user.perfil

    numero = agendamento.cliente.telefone
    # Garantir que o número esteja no formato internacional com '+'
    if not numero.startswith('+'):
        numero = '+55' + numero.lstrip('0').replace(' ', '').replace('-', '')
    mensagem = f'Olá {agendamento.cliente.nome}, você tem um agendamento para {agendamento.data_hora_inicio.strftime("%d/%m/%Y às %H:%M")} no {perfil.nome_salao}.'
    try:
        print(f"Número: {numero} Mensagem: {mensagem}")
        enviar_sms(numero, mensagem)
        messages.info(request, 'Lembrete SMS enviado.')
    except Exception as e:
        print("Erro ao tentar enviar SMS:")
        print(f"Nome: {agendamento.cliente.nome}")
        print(f"Telefone: {numero}")
        print(f"Mensagem: {mensagem}")
        print(f"Exceção: {e}")
        messages.warning(request, 'Falha ao enviar SMS')

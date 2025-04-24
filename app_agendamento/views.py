from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from app_agendamento.forms import ClienteForm, AgendamentoForm
from app_agendamento.models import Cliente, Agendamento


def agendamento(request):
    agendamentos = Agendamento.objects.all().order_by('-data_hora_inicio')
    todos_clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'agenda/agenda.html', {
        'agendamentos': agendamentos,
        'todos_clientes': todos_clientes
    })


def cadastrar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()

            query_params = request.GET.urlencode()
            url = reverse('agendamento')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect(url)
    else:
        form = AgendamentoForm()
    return render(request, 'agenda/agenda.html', {'form': form})


def obter_agendamento(request, id_agendamento):
    agendamento_consultado = get_object_or_404(Agendamento, id=id_agendamento)

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
        'observacoes': agendamento_consultado.observacoes if agendamento_consultado.observacoes else '',
        'status': agendamento_consultado.status,
        'status_display': agendamento_consultado.get_status_display(),
    }

    return JsonResponse(dados)


def editar_agendamento(request, id_agendamento):
    agendamento_consultado = get_object_or_404(Agendamento, id=id_agendamento)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento_consultado)
        if form.is_valid():
            form.save()

            query_params = request.GET.urlencode()
            url = reverse('agendamento')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Agendamento alterado com sucesso!')
            return redirect(url)
    return redirect('agendamento')


def remover_agendamento(request, id_agendamento):
    agendamento_consultado = get_object_or_404(Agendamento, id=id_agendamento)
    agendamento_consultado.delete()
    messages.success(request, 'Agendamento removido com sucesso!')
    return redirect('agendamento')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('lista_clientes')
            if query_params:
                url += f'?{query_params}'

            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect(url)
    else:
        form = ClienteForm()
    return render(request, 'agenda/listar_clientes.html', {'form': form})


def listar_clientes(request):
    termo = request.GET.get('criterio', '')

    if termo:
        clientes = Cliente.objects.filter(nome__icontains=termo).order_by('-data_cadastro')
    else:
        clientes = Cliente.objects.all().order_by('-data_cadastro')

    return render(
        request,
        'agenda/listar_clientes.html',
        {
            'clientes': clientes,
            'termo': termo
        }
    )


def obter_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    dados = {
        'id': cliente.id,
        'nome': cliente.nome,
        'telefone': cliente.telefone,
        'email': cliente.email if cliente.email else '',
        'data_cadastro': cliente.data_cadastro.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return JsonResponse(dados)


def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)

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
    return redirect('lista_clientes')


def remover_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)

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


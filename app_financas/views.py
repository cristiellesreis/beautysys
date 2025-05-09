from calendar import month_name

from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.timezone import now

from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa


def financas(request):
    return render(request, 'financas/financas.html')


def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_receitas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect(url)
    else:
        form = ReceitaForm()
    return render(request, 'financas/listar_receitas.html', {'form': form})


def listar_receitas(request):
    termo = request.GET.get('criterio', '')
    if termo:
        receitas = Receita.objects.filter(descricao__icontains=termo).order_by('-data')
    else:
        receitas = Receita.objects.all().order_by('-data')
    return render(request, 'financas/listar_receitas.html', {'receitas': receitas, 'termo': termo})


def remover_receita(request, id_receita):
    receita = get_object_or_404(Receita, id=id_receita)
    receita.delete()
    query_params = request.GET.urlencode()
    url = reverse('listar_receitas')
    if query_params:
        url += f'?{query_params}'
    messages.success(request, 'Receita removida com sucesso!')
    return redirect(url)


def obter_receita(request, id_receita):
    receita = get_object_or_404(Receita, id=id_receita)
    dados = {
        'id': receita.id,
        'descricao': receita.descricao,
        'valor': str(receita.valor),
        'data': receita.data.strftime('%Y-%m-%d'),
    }
    return JsonResponse(dados)


def editar_receita(request, id_receita):
    receita = get_object_or_404(Receita, id=id_receita)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_receitas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Receita alterada com sucesso!')
            return redirect(url)
    return redirect('listar_receitas')


def cadastrar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_despesas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Despesa cadastrada com sucesso!')
            return redirect(url)
    else:
        form = DespesaForm()
    return render(request, 'financas/listar_despesas.html', {'form': form})


def listar_despesas(request):
    termo = request.GET.get('criterio', '')
    if termo:
        despesas = Despesa.objects.filter(descricao__icontains=termo).order_by('-data')
    else:
        despesas = Despesa.objects.all().order_by('-data')

    return render(request, 'financas/listar_despesas.html', {'despesas': despesas, 'termo': termo})


def remover_despesa(request, id_despesa):
    despesa = get_object_or_404(Despesa, id=id_despesa)
    despesa.delete()
    query_params = request.GET.urlencode()
    url = reverse('listar_despesas')
    if query_params:
        url += f'?{query_params}'
    messages.success(request, 'Despesa removida com sucesso!')
    return redirect(url)


def obter_despesa(request, id_despesa):
    despesa = get_object_or_404(Despesa, id=id_despesa)
    dados = {
        'id': despesa.id,
        'descricao': despesa.descricao,
        'valor': str(despesa.valor),
        'data': despesa.data.strftime('%Y-%m-%d'),
    }
    return JsonResponse(dados)


def editar_despesa(request, id_despesa):
    despesa = get_object_or_404(Despesa, id=id_despesa)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_despesas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Despesa alterada com sucesso!')
            return redirect(url)
    return redirect('listar_despesas')


def grafico_receitas_despesas_mensal(request):
    meses = range(1, 13)
    ano_atual = now().year

    nomes_meses_ptbr = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    receitas = []
    despesas = []

    for mes in meses:
        nome_mes = nomes_meses_ptbr[mes - 1]
        total_receitas = Receita.objects.filter(data__year=ano_atual, data__month=mes).aggregate(Sum('valor'))['valor__sum'] or 0
        total_despesas = Despesa.objects.filter(data__year=ano_atual, data__month=mes).aggregate(Sum('valor'))['valor__sum'] or 0

        receitas.append({'name': nome_mes, 'y': float(total_receitas)})
        despesas.append({'name': nome_mes, 'y': float(total_despesas)})

    dados = {
        "receitas": receitas,
        "despesas": despesas
    }

    return JsonResponse(dados)

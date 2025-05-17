from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.timezone import now

from app_perfil.models import Perfil
from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa


@login_required
def financas(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    hoje = now()
    mes_atual = hoje.month
    ano_atual = hoje.year

    total_receita_mes = Receita.objects.filter(
        perfil=perfil, data__year=ano_atual, data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    total_despesa_mes = Despesa.objects.filter(
        perfil=perfil, data__year=ano_atual, data__month=mes_atual
    ).aggregate(total=Sum('valor'))['total'] or 0

    margem_lucro = total_receita_mes - total_despesa_mes

    return render(request, 'financas/financas.html', {
        'total_receita_mes': total_receita_mes,
        'total_despesa_mes': total_despesa_mes,
        'margem_lucro': margem_lucro,
    })


@login_required
def cadastrar_receita(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.perfil = perfil
            receita.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_receitas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect(url)
    else:
        form = ReceitaForm()
    return render(request, 'financas/listar_receitas.html', {'form': form})


@login_required
def listar_receitas(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    termo = request.GET.get('criterio', '')
    if termo:
        receitas = Receita.objects.filter(perfil=perfil, descricao__icontains=termo).order_by('-data')
    else:
        receitas = Receita.objects.filter(perfil=perfil).order_by('-data')
    return render(request, 'financas/listar_receitas.html', {'receitas': receitas, 'termo': termo})


@login_required
def remover_receita(request, id_receita):
    perfil = get_object_or_404(Perfil, user=request.user)
    receita = get_object_or_404(Receita, id=id_receita, perfil=perfil)
    receita.delete()
    query_params = request.GET.urlencode()
    url = reverse('listar_receitas')
    if query_params:
        url += f'?{query_params}'
    messages.success(request, 'Receita removida com sucesso!')
    return redirect(url)


@login_required
def obter_receita(request, id_receita):
    perfil = get_object_or_404(Perfil, user=request.user)
    receita = get_object_or_404(Receita, id=id_receita, perfil=perfil)

    dados_receita = {
        'id': receita.id,
        'descricao': receita.descricao,
        'valor': float(receita.valor),
        'data': receita.data.strftime('%Y-%m-%d'),
    }

    return JsonResponse(dados_receita)


@login_required
def editar_receita(request, id_receita):
    perfil = get_object_or_404(Perfil, user=request.user)
    receita = get_object_or_404(Receita, id=id_receita, perfil=perfil)
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


@login_required
def cadastrar_despesa(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.perfil = perfil
            despesa.save()
            query_params = request.GET.urlencode()
            url = reverse('listar_despesas')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Despesa cadastrada com sucesso!')
            return redirect(url)
    else:
        form = DespesaForm()
    return render(request, 'financas/listar_despesas.html', {'form': form})


@login_required
def listar_despesas(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    termo = request.GET.get('criterio', '')
    if termo:
        despesas = Despesa.objects.filter(perfil=perfil, descricao__icontains=termo).order_by('-data')
    else:
        despesas = Despesa.objects.filter(perfil=perfil).order_by('-data')

    return render(request, 'financas/listar_despesas.html', {'despesas': despesas, 'termo': termo})


@login_required
def remover_despesa(request, id_despesa):
    perfil = get_object_or_404(Perfil, user=request.user)
    despesa = get_object_or_404(Despesa, id=id_despesa, perfil=perfil)
    despesa.delete()
    query_params = request.GET.urlencode()
    url = reverse('listar_despesas')
    if query_params:
        url += f'?{query_params}'
    messages.success(request, 'Despesa removida com sucesso!')
    return redirect(url)


@login_required
def obter_despesa(request, id_despesa):
    perfil = get_object_or_404(Perfil, user=request.user)
    despesa = get_object_or_404(Despesa, id=id_despesa, perfil=perfil)

    dados_despesa = {
        'id': despesa.id,
        'descricao': despesa.descricao,
        'valor': float(despesa.valor),
        'data': despesa.data.strftime('%Y-%m-%d'),
    }

    return JsonResponse(dados_despesa)


@login_required
def editar_despesa(request, id_despesa):
    perfil = get_object_or_404(Perfil, user=request.user)
    despesa = get_object_or_404(Despesa, id=id_despesa, perfil=perfil)
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


@login_required
def grafico_receitas_despesas_mensal(request):
    perfil = get_object_or_404(Perfil, user=request.user)
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
        total_receitas = Receita.objects.filter(perfil=perfil, data__year=ano_atual, data__month=mes).aggregate(Sum('valor'))['valor__sum'] or 0
        total_despesas = Despesa.objects.filter(perfil=perfil, data__year=ano_atual, data__month=mes).aggregate(Sum('valor'))['valor__sum'] or 0

        receitas.append({'name': nome_mes, 'y': float(total_receitas)})
        despesas.append({'name': nome_mes, 'y': float(total_despesas)})

    dados = {
        "receitas": receitas,
        "despesas": despesas
    }

    return JsonResponse(dados)

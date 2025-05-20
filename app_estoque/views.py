from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from app_perfil.models import Perfil
from .forms import ItemEstoqueForm
from .models import ItemEstoque


@login_required
def estoque(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    termo = request.GET.get('criterio', '')

    if termo:
        itens = ItemEstoque.objects.filter(perfil=perfil, nome__icontains=termo).order_by('nome')
    else:
        itens = ItemEstoque.objects.filter(perfil=perfil).order_by('nome')

    return render(request, 'estoque/estoque.html', {'itens': itens, 'termo': termo})


@login_required
def cadastrar_item_estoque(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.perfil = perfil
            item.save()
            messages.success(request, 'Item cadastrado com sucesso!')
            return redirect('estoque')
    else:
        form = ItemEstoqueForm()
    return render(request, 'estoque/estoque.html', {'form': form})


@login_required
def remover_item_estoque(request, id_item_estoque):
    perfil = get_object_or_404(Perfil, user=request.user)
    item = get_object_or_404(ItemEstoque, id=id_item_estoque, perfil=perfil)
    item.delete()
    query_params = request.GET.urlencode()
    url = reverse('estoque')
    if query_params:
        url += f'?{query_params}'
    messages.success(request, 'Item de estoque removido com sucesso!')
    return redirect(url)


@login_required
def obter_item_estoque(request, id_item_estoque):
    perfil = get_object_or_404(Perfil, user=request.user)
    item = get_object_or_404(ItemEstoque, id=id_item_estoque, perfil=perfil)

    dados_item = {
        'id': item.id,
        'nome': item.nome,
        'quantidade': item.quantidade,
        'preco_aquisicao': float(item.preco_aquisicao),
        'preco_venda': float(item.preco_venda),
        'data_validade': item.data_validade.strftime('%Y-%m-%d') if item.data_validade else '',
    }

    return JsonResponse(dados_item)


@login_required
def editar_item_estoque(request, id_item_estoque):
    perfil = get_object_or_404(Perfil, user=request.user)
    item = get_object_or_404(ItemEstoque, id=id_item_estoque, perfil=perfil)

    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            query_params = request.GET.urlencode()
            url = reverse('estoque')
            if query_params:
                url += f'?{query_params}'
            messages.success(request, 'Item de estoque alterado com sucesso!')
            return redirect(url)

    return redirect('estoque')

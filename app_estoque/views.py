from django.shortcuts import render, redirect
from .models import Item_Estoque
from .services import EstoqueService
from .forms import ItemEstoqueForm
from .exceptions import QuantidadeInsuficiente
from django.http import JsonResponse

def estoque(request):
    lista_estoque = {}
    form = ItemEstoqueForm()
    try:
        lista_estoque = EstoqueService.obter_itens_estoque()
        return render(request, 'estoque/estoque.html', {'itens_estoque' : lista_estoque,'form': form})
    except Item_Estoque.DoesNotExist:
        return render(request, 'estoque/estoque.html')
    
    
def adicionar_item_estoque(request):
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            EstoqueService.adicionar_item(
                nome=form.cleaned_data['item'],
                quantidade=form.cleaned_data['quantidade']
            )
            return redirect('estoque')
    
def remove_item_estoque(request,pk):
    exception = {}
    if request.method == 'POST':
        try:
            quantidade = int(request.POST.get('quantidade'),0)
            EstoqueService.remover_item(request, pk, quantidade)
        except QuantidadeInsuficiente as e:
            return JsonResponse({'erro': str(e)}, status=400)
        
        return redirect('estoque')
    
    return redirect('estoque')
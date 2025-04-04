from django.shortcuts import render, redirect
from .models import Item_Estoque
from .services import EstoqueService
from .forms import ItemEstoqueForm

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
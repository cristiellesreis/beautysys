from django import forms
from .models import ItemEstoque


class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = ['nome', 'quantidade', 'preco_aquisicao', 'preco_venda', 'data_validade']

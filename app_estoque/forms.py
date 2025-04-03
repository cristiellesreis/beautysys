from django import forms
from .models import Item_Estoque

class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = Item_Estoque
        fields = ['item','quantidade']
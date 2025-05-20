from django import forms
from .models import Receita, Despesa


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao','categoria','valor', 'data']


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao','categoria','valor', 'data']

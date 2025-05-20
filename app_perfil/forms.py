from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_salao', 'telefone', 'cnpj', 'endereco', 'cidade', 'estado', 'cep', 'imagem']
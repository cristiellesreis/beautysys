from django import forms
from .models import Cliente, Agendamento


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'data_hora_inicio', 'data_hora_fim', 'servico', 'observacoes', 'status', 'lembrete_sms']
        widgets = {
            'data_hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_hora_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

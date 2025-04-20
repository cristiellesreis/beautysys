from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    objects: models.Manager["Cliente"]

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='agendamentos'
    )
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    servico = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='agendado')

    objects: models.Manager["Agendamento"]

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_hora_inicio.strftime('%d/%m/%Y %H:%M')}"

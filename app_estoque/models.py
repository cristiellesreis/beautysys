from django.db import models

from app_perfil.models import Perfil


class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco_aquisicao = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_validade = models.DateTimeField(blank=True, null=True)

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='itens_estoque'
    )

    objects: models.Manager["ItemEstoque"]

    def __str__(self):
        return self.nome

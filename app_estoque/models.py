from django.db import models

class Item_Estoque(models.Model):
    item = models.CharField(max_length=50)
    entrada_no_estoque = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    custo_aquisicao = models.DecimalField(max_digits=8, decimal_places=2)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    
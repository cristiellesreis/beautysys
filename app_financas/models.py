from django.db import models

from app_perfil.models import Perfil


class Receita(models.Model):
    CATEGORIAS = [
        ('cortes', 'Cortes'),
        ('tratamento', 'Tratamento'),
        ('finalizacao', 'Finalização'),
        ('quimica', 'Química'),
        ('outros', 'Outros'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='receitas')
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outros')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    objects: models.Manager["Receita"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class Despesa(models.Model):
    CATEGORIAS = [
        ('custos fixos', 'custos fixos'),
        ('produtos', 'produtos'),
        ('salario', 'salario'),
        ('outros', 'outros'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='despesas')
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outros')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    objects: models.Manager["Despesa"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

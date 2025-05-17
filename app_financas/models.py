from django.db import models

from django.db import models

class Receita(models.Model):
    CATEGORIAS = [
    ('cortes', 'Cortes'),
    ('tratamento', 'Tratamento'),
    ('finalizacao', 'Finalização'),
    ('quimica', 'Química'),
    ('outros', 'Outros'),
]

    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outros')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class Despesa(models.Model):
    CATEGORIAS = [
    ('custos fixos', 'custos fixos'),
    ('produtos', 'produtos'),
    ('salario', 'salario'),
    ('outros', 'outros'),
]
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='outros')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    objects: models.Manager["Despesa"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

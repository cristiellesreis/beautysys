from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    objects: models.Manager["Receita"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"


class Despesa(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    objects: models.Manager["Despesa"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

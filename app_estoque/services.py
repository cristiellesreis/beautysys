from .models import Item_Estoque

class EstoqueService:
    @staticmethod
    def obter_itens_estoque():
        return Item_Estoque.objects.all()

    @staticmethod
    def adicionar_item(nome, quantidade):
        Item_Estoque.objects.create(
            item=nome,
            quantidade=quantidade,
            )
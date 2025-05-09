from django.contrib import admin
from .models import Item_Estoque

@admin.register(Item_Estoque)
class ItemEstoqueAdmin(admin.ModelAdmin):
    list_display = ('item', 'entrada_no_estoque', 'quantidade', 'preco')
    list_filter = ('entrada_no_estoque',)
    search_fields = ('item',)

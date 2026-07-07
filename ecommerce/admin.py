from django.contrib import admin
from .models import Producto, Pedido, ItemPedido


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "stock",
        "activo",
    )

    list_filter = ("activo",)

    search_fields = ("nombre",)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "fecha",
        "total",
    )

    inlines = [
        ItemPedidoInline,
    ]

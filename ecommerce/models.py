from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.TextField("Descripción")
    precio = models.PositiveIntegerField("Precio")
    stock = models.PositiveIntegerField("Stock")
    imagen = models.ImageField("Imagen", upload_to="productos/", null=True, blank=True)
    ## Este campo indica si el producto está activo o no, lo que permite ocultarlo de la tienda sin eliminarlo de la base de datos.
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")
    fecha = models.DateTimeField("Fecha de pedido", auto_now_add=True)
    total = models.DecimalField("Total", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-fecha"]

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField("Cantidad")
    precio = models.PositiveIntegerField("Precio")

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Items de Pedido"

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
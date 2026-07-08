from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from ecommerce.forms import ProductoForm
from .models import Producto, Pedido, ItemPedido
from .carrito import Carrito


class HomeView(TemplateView):
    template_name = "ecommerce/home.html"


class ProductListView(ListView):
    model = Producto
    template_name = "ecommerce/product_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(activo=True)


class ProductDetailView(DetailView):
    model = Producto
    template_name = "ecommerce/product_detail.html"
    context_object_name = "producto"


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class ProductCreateView(
    AdminRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):

    model = Producto

    form_class = ProductoForm

    template_name = "ecommerce/product_form.html"

    success_url = reverse_lazy("ecommerce:product_list")

    success_message = "Producto creado correctamente."


class ProductUpdateView(
    AdminRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):

    model = Producto

    form_class = ProductoForm

    template_name = "ecommerce/product_form.html"

    success_url = reverse_lazy("ecommerce:product_list")

    success_message = "Producto actualizado correctamente."


class ProductDeleteView(
    AdminRequiredMixin,
    DeleteView,
):

    model = Producto

    template_name = "ecommerce/product_confirm_delete.html"

    success_url = reverse_lazy("ecommerce:product_list")


class PedidoExitosoView(LoginRequiredMixin, DetailView):
    template_name = "ecommerce/pedido_exitoso.html"
    model = Pedido
    context_object_name = "pedido"

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)


def agregar_al_carrito(request, producto_id):
    print("entre a agregar")
    carrito = Carrito(request)

    producto = get_object_or_404(
        Producto,
        pk=producto_id,
        activo=True,
    )

    agregado = carrito.agregar(producto)

    if agregado:
        messages.success(request, f'"{producto.nombre}" fue agregado al carrito.')
    else:
        messages.warning(
            request, f'No hay más stock disponible para "{producto.nombre}".'
        )

    return redirect("ecommerce:product_list")


def ver_carrito(request):
    return render(
        request,
        "ecommerce/carrito.html",
    )


def eliminar_del_carrito(request, producto_id):

    carrito = Carrito(request)

    producto = get_object_or_404(
        Producto,
        pk=producto_id,
    )

    carrito.eliminar(producto)

    return redirect("ecommerce:carrito")


def restar_del_carrito(request, producto_id):

    carrito = Carrito(request)

    producto = get_object_or_404(
        Producto,
        pk=producto_id,
    )

    carrito.restar(producto)

    return redirect("ecommerce:carrito")


def limpiar_carrito(request):

    carrito = Carrito(request)

    carrito.limpiar()

    return redirect("ecommerce:carrito")


def agregar_desde_carrito(request, producto_id):

    carrito = Carrito(request)

    producto = get_object_or_404(
        Producto,
        pk=producto_id,
        activo=True,
    )

    carrito.agregar(producto)
    return redirect("ecommerce:carrito")


@login_required
def confirmar_compra(request):

    carrito = Carrito(request)

    if not carrito.carrito:

        messages.warning(request, "El carrito está vacío.")

        return redirect("ecommerce:carrito")

    with transaction.atomic():

        pedido = Pedido.objects.create(
            usuario=request.user,
            total=0,
        )
        total = 0

        for item in carrito.carrito.values():

            producto = Producto.objects.get(pk=item["id"])

            if producto.stock < item["cantidad"]:

                messages.error(
                    request, f"No hay stock suficiente para {producto.nombre}."
                )

                return redirect("ecommerce:carrito")

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item["cantidad"],
                precio=producto.precio,
            )

            producto.stock -= item["cantidad"]

            producto.save()

            total += producto.precio * item["cantidad"]
        pedido.total = total
        pedido.save()
    carrito.vaciar()

    messages.success(request, "¡Compra realizada correctamente!")

    return redirect(
        "ecommerce:pedido_exitoso",
        pk=pedido.pk,
    )

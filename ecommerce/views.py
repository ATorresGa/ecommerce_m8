from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from ecommerce.forms import ProductoForm
from .models import Producto


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
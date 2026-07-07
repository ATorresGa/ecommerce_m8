from django.views.generic import TemplateView, ListView, DetailView
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
    
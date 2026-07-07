from django.urls import path

from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "ecommerce"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "productos/",
        ProductListView.as_view(),
        name="product_list",
    ),
    path(
        "producto/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "productos/nuevo/",
        ProductCreateView.as_view(),
        name="product_create",
    ),
    path(
        "productos/<int:pk>/editar/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "productos/<int:pk>/eliminar/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
]

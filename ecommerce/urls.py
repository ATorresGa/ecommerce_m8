from django.urls import path

from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    agregar_al_carrito,
    ver_carrito,
    eliminar_del_carrito,
    limpiar_carrito,
    restar_del_carrito,
    agregar_desde_carrito,
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
    path(
        "carrito/agregar/<int:producto_id>/",
        agregar_al_carrito,
        name="agregar_carrito",
    ),
    path(
        "carrito/",
        ver_carrito,
        name="carrito",
    ),
    path(
        "carrito/eliminar/<int:producto_id>/",
        eliminar_del_carrito,
        name="eliminar_carrito",
    ),
    path(
        "carrito/restar/<int:producto_id>/",
        restar_del_carrito,
        name="restar_carrito",
    ),
    path(
        "carrito/limpiar/",
        limpiar_carrito,
        name="limpiar_carrito",
    ),
    path(
        "carrito/agregar_desde_carrito/<int:producto_id>/",
        agregar_desde_carrito,
        name="agregar_desde_carrito",
    ),
]

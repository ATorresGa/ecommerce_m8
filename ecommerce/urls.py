from django.urls import path

from .views import HomeView, ProductListView, ProductDetailView

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
]

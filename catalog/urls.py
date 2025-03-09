from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    home,
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products_list/", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("products/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"
    ),
]

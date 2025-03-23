from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    home,
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    UnpublishProductView,
    ProductByCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products_list/", ProductListView.as_view(), name="products_list"),
    path(
        "products/<int:pk>",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("products/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "unpublish/<int:pk>/", UnpublishProductView.as_view(), name="unpublish_product"
    ),
    path(
        "category/<int:pk>/",
        ProductByCategoryView.as_view(),
        name="products_list_by_category",
    ),
]

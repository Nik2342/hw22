from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm, ProductModerationForm
from catalog.models import Product
from catalog.services import (
    get_products_from_cache,
    get_products_by_category_from_cache,
)


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModerationForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "У вас недостаточно прав для снятия продукта с публикации"
            )

        product.is_published = False
        product.save()

        return redirect("catalog:products", pk=product.id)


class ProductByCategoryView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_by_category_from_cache()

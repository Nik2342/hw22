from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ("title", "content","preview_image")
    success_url = reverse_lazy("catalog:products_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description","price")
    success_url = reverse_lazy("catalog:products_list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
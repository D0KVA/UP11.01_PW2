from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
def general_view(request):
    return render(request, 'general.html')

def company_view(request):
    return render(request, 'company.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def places_view(request):
    return render(request, 'places.html')

def items_view(request):
    return render(request, 'items.html')

def category_view(request):
    return render(request, 'category.html')

def all_view(request):
    return render(request, 'all.html')

def basket_view(request):
    return render(request, 'basket.html')

class ItemsListView(ListView):
    model = Items
    template_name = 'items/items_list.html'
    context_object_name = 'items'

class ItemsDetailView(DetailView):
    model = Items
    template_name = 'items/items_detail.html'
    context_object_name = 'items'

class ItemsCreateView(CreateView):
    model = Items
    form_class = ItemsForm
    template_name = 'items/items_form.html'
    success_url= reverse_lazy('product_list_view')

class ItemsUpdateView(UpdateView):
    model = Items
    form_class = ItemsForm
    template_name = 'items/items_form.html'
    success_url= reverse_lazy('product_list_view')

class ItemsDeleteView(DeleteView):
    model = Items
    template_name = 'items/items_confirm_delete.html'
    success_url= reverse_lazy('product_list_view')


class SuppliersListView(ListView):
    model = Supplier
    template_name = 'suppliers/suppliers_list.html'
    context_object_name = 'supplier'

class SuppliersDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers/suppliers_detail.html'
    context_object_name = 'supplier'

class SuppliersCreateView(CreateView):
    model = Supplier
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url= reverse_lazy('suppliers_list_view')

class SuppliersUpdateView(UpdateView):
    model = Supplier
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url= reverse_lazy('suppliers_list_view')

class SuppliersDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers/suppliers_confirm_delete.html'
    success_url= reverse_lazy('suppliers_list_view')


class BrandsListView(ListView):
    model = Brand
    template_name = 'brands/brands_list.html'
    context_object_name = 'brand'

class BrandsDetailView(DetailView):
    model = Brand
    template_name = 'brands/brands_detail.html'
    context_object_name = 'brand'

class BrandsCreateView(CreateView):
    model = Brand
    form_class = BrandsForm
    template_name = 'brands/brands_form.html'
    success_url= reverse_lazy('brands_list_view')

class BrandsUpdateView(UpdateView):
    model = Brand
    form_class = BrandsForm
    template_name = 'brands/brands_form.html'
    success_url= reverse_lazy('brands_list_view')

class BrandsDeleteView(DeleteView):
    model = Brand
    template_name = 'brands/brands_confirm_delete.html'
    success_url= reverse_lazy('brands_list_view')


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'category'

class CategoriesDetailView(DetailView):
    model = Category
    template_name = 'categories/categories_detail.html'
    context_object_name = 'category'

class CategoriesCreateView(CreateView):
    model = Category
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url= reverse_lazy('categories_list_view')

class CategoriesUpdateView(UpdateView):
    model = Category
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url= reverse_lazy('categories_list_view')

class CategoriesDeleteView(DeleteView):
    model = Category
    template_name = 'categories/categories_confirm_delete.html'
    success_url= reverse_lazy('categories_list_view')


class CollectionsListView(ListView):
    model = Collection
    template_name = 'collections/collections_list.html'
    context_object_name = 'collection'

class CollectionsDetailView(DetailView):
    model = Collection
    template_name = 'collections/collections_detail.html'
    context_object_name = 'collection'

class CollectionsCreateView(CreateView):
    model = Collection
    form_class = CollectionsForm
    template_name = 'collections/collections_form.html'
    success_url= reverse_lazy('collections_list_view')

class CollectionsUpdateView(UpdateView):
    model = Collection
    form_class = CollectionsForm
    template_name = 'collections/collections_form.html'
    success_url= reverse_lazy('collections_list_view')

class CollectionsDeleteView(DeleteView):
    model = Collection
    template_name = 'collections/collections_confirm_delete.html'
    success_url= reverse_lazy('collections_list_view')


class CustomersListView(ListView):
    model = Customer
    template_name = 'customers/customers_list.html'
    context_object_name = 'customer'

class CustomersDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers_detail.html'
    context_object_name = 'customer'

class CustomersCreateView(CreateView):
    model = Customer
    form_class = CustomersForm
    template_name = 'customers/customers_form.html'
    success_url= reverse_lazy('customers_list_view')

class CustomersUpdateView(UpdateView):
    model = Customer
    form_class = CustomersForm
    template_name = 'customers/customers_form.html'
    success_url= reverse_lazy('customers_list_view')

class CustomersDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers_confirm_delete.html'
    success_url= reverse_lazy('customers_list_view')
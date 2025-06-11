from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('general/', general_view, name='general_view'),
    path('company/', company_view, name='company_view'),
    path('company/contacts/', contacts_view, name='contacts_view'),
    path('company/places/', places_view, name='places_view'),
    path('items/', items_view, name='items_view'),
    path('items/category/', category_view, name='category_view'),
    path('items/all/', all_view, name='all_view'),
    path('basket/', basket_view, name='basket_view'),

    path('', ItemsListView.as_view(), name='product_list_view'),
    path('products/<int:pk>/', ItemsDetailView.as_view(), name='items_detail_view'),
    path('products/create/', ItemsCreateView.as_view(), name='items_create_view'),
    path('products/<int:pk>/update', ItemsUpdateView.as_view(), name='items_update_view'),
    path('products/<int:pk>/delete', ItemsDeleteView.as_view(), name='items_delete_view'),

    path('suppliers/', SuppliersListView.as_view(), name='suppliers_list_view'),
    path('suppliers/<int:pk>/', SuppliersDetailView.as_view(), name='suppliers_detail_view'),
    path('suppliers/create/', SuppliersCreateView.as_view(), name='suppliers_create_view'),
    path('suppliers/<int:pk>/update', SuppliersUpdateView.as_view(), name='suppliers_update_view'),
    path('suppliers/<int:pk>/delete', SuppliersDeleteView.as_view(), name='suppliers_delete_view'),

    path('brands/', BrandsListView.as_view(), name='brands_list_view'),
    path('brands/<int:pk>/', BrandsDetailView.as_view(), name='brands_detail_view'),
    path('brands/create/', BrandsCreateView.as_view(), name='brands_create_view'),
    path('brands/<int:pk>/update', BrandsUpdateView.as_view(), name='brands_update_view'),
    path('brands/<int:pk>/delete', BrandsDeleteView.as_view(), name='brands_delete_view'),

    path('categories/', CategoriesListView.as_view(), name='categories_list_view'),
    path('categories/<int:pk>/', CategoriesDetailView.as_view(), name='categories_detail_view'),
    path('categories/create/', CategoriesCreateView.as_view(), name='categories_create_view'),
    path('categories/<int:pk>/update', CategoriesUpdateView.as_view(), name='categories_update_view'),
    path('categories/<int:pk>/delete', CategoriesDeleteView.as_view(), name='categories_delete_view'),

    path('collections/', CollectionsListView.as_view(), name='collections_list_view'),
    path('collections/<int:pk>/', CollectionsDetailView.as_view(), name='collections_detail_view'),
    path('collections/create/', CollectionsCreateView.as_view(), name='collections_create_view'),
    path('collections/<int:pk>/update', CollectionsUpdateView.as_view(), name='collections_update_view'),
    path('collections/<int:pk>/delete', CollectionsDeleteView.as_view(), name='collections_delete_view'),

    path('customers/', CustomersListView.as_view(), name='customers_list_view'),
    path('customers/<int:pk>/', CustomersDetailView.as_view(), name='customers_detail_view'),
    path('customers/create/', CustomersCreateView.as_view(), name='customers_create_view'),
    path('customers/<int:pk>/update', CustomersUpdateView.as_view(), name='customers_update_view'),
    path('customers/<int:pk>/delete', CustomersDeleteView.as_view(), name='customers_delete_view'),
]

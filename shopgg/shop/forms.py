from django import forms
from .models import *

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'photo', 'is_exists', 'category', 'collection', 'brand', 'supplier']

class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'photo']

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CollectionsForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']

class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']
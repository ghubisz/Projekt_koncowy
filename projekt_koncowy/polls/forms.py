from django import forms
from .models import Category


class AddProductForm(forms.Form):
    name = forms.CharField(label='Name of product', max_length=100)
    name.widget.attrs.update({'placeholder': 'Name of new item'})
    description = forms.CharField(label='Description', max_length=100)
    description.widget.attrs.update({'placeholder': 'Description of new item'})
    price = forms.FloatField(label='Price', required=True, max_value=1000, min_value=0.01)
    price.widget.attrs.update({'id': 'price', 'step': "0.01"})
    quantity = forms.FloatField(label='Quantity', required=True, max_value=100, min_value=1)
    quantity.widget.attrs.update({'id': 'quantity', 'step': "1"})
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all().order_by('name'))
    category.widget.attrs.update({'id': 'assigned_category'})


class AddCategoryForm(forms.Form):
    name = forms.CharField(label='Category name', max_length=100)
    name.widget.attrs.update({'placeholder': 'Name of new category'})

from django import forms
from django.forms import ModelChoiceField

from .models import Product, Supplier

class MenuModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return "Supplier %s" % (obj.name)

class ProductForm(forms.ModelForm):

    supplier = MenuModelChoiceField(queryset=Supplier.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'brand', 'supplier', 'current_amount', 'product_state', 'registration_date', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product\'s name'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Brand\'s name'}),
            'current_amount': forms.NumberInput(attrs={'placeholder': 'Product\'s current amount'}),
            'product_state': forms.Select(choices=Product.PRODUCT_STATE),
            'registration_date': forms.SelectDateWidget(),
            'description': forms.Textarea(attrs={'placeholder': 'Write a description for the product'}),
        }


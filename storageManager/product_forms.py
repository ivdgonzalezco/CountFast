from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'brand', 'current_amount', 'product_state', 'registration_date', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product\'s name'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Brand\'s name'}),
            'current_amount': forms.NumberInput(attrs={'placeholder': 'Product\'s current amount'}),
            'product_state': forms.Select(choices=Product.PRODUCT_STATE),
            'registration_date': forms.SelectDateWidget(),
            'description': forms.Textarea(attrs={'placeholder': 'Write a description for the product'}),
        }


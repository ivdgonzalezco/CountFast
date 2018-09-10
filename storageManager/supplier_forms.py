from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('nit', 'name', 'supplier_state', 'registration_date')
        widgets = {
            'nit': forms.TextInput(attrs={'placeholder': 'Supplier\'s identification number'}),
            'name': forms.TextInput(attrs={'placeholder': 'Supplier\'s name'}),
            'supplier_state': forms.Select(choices=Supplier.SUPPLIER_STATE),
            'registration_date': forms.SelectDateWidget(),
        }
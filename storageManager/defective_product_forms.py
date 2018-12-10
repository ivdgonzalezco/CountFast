from django import forms
from django.forms import ModelChoiceField

from .models import DefectiveProducts, Product

class MenuModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return "Product %s" % (obj.name)

class DefectiveProductForm(forms.ModelForm):

    product = MenuModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = DefectiveProducts
        fields = ('quantity', 'registration_date', 'failed_description', 'product')
        widgets = {
            'quantity': forms.NumberInput(attrs={'placeholder': 'Defective Product\'s quantity'}),
            'registration_date': forms.SelectDateWidget(),
            'failed_description': forms.Textarea(attrs={'placeholder': 'Failed Description'}),
        }


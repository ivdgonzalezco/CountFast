from django import forms
from django.forms import ModelChoiceField

from .models import Movement, Product

class MenuModelChoiceField(ModelChoiceField):

    def label_from_instance(Product, obj):
        return  (obj.id)

class MovementForm(forms.ModelForm):

    id_product = MenuModelChoiceField(queryset=Product.objects.all())
   
	
    class Meta:
        model = Movement
        fields = ('quantity', 'id_user_register', 'register_date','id_product')
        widgets = {
			'quantity': forms.NumberInput(attrs={'placeholder': 'Movement\'s quantity'}),
			'id_user_register': forms.NumberInput(attrs={'placeholder': 'Movement\'s id user register'}),
			'register_date': forms.SelectDateWidget(),		
			
        }


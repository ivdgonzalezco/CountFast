from django import forms
from django.forms import ModelChoiceField

from .models import Move, Product


class MenuModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return "Product %s" % (obj.name)


class MoveForm(forms.ModelForm):

    product = MenuModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Move
        fields = ('move_state', 'quantity', 'registration_date', 'product')
        widgets = {
            'move_state': forms.Select(choices=Move.MOVE_STATE),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Movement\'s quantity'}),
            'registration_date': forms.SelectDateWidget(),
        }

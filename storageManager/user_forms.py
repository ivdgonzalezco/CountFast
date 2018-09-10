from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'login', 'password', 'user_role', 'user_state')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'User\'s name'}),
            'login': forms.TextInput(attrs={'placeholder': 'User\'s Login'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'User\'s password'}),
            'user_role': forms.Select(choices=User.USER_ROLE),
            'user_state': forms.Select(choices=User.USER_STATE),
        }
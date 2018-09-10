from django import forms
from .models import User
import re

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

    def clean(self):
        password = self.cleaned_data.get('password')
        length_regex = re.compile(r'.{8,}')
        uppercase_regex = re.compile(r'[A-Z]')
        lowercase_regex = re.compile(r'[a-z]')
        digit_regex = re.compile(r'[0-9]')

        is_password_valid = (length_regex.search(password) is not None
                and uppercase_regex.search(password) is not None
                and lowercase_regex.search(password) is not None
                and digit_regex.search(password) is not None)

        if not is_password_valid:
            raise forms.ValidationError(
                "Password validation failed (min length=8, min one uppercase letter, min one lowercase letter, min one digit)"
            )


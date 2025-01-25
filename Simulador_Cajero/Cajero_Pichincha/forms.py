# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Account

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'identification', 'password1', 'password2')

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('account_number', 'account_type', 'funds')
        
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
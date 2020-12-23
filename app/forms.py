from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control mb-3"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3"
    }))
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
from django import forms
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'document']

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(help_text='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
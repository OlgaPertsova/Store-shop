from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Иван"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Иванов"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "you@mail.com"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Россия, Москва, ул.Мира, дом 6"}))



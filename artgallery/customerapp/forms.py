from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone', 'altphone', 'email', 'pincode', 'address']
    price = forms.DecimalField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.HiddenInput())

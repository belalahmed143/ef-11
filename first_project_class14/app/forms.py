from django import forms
from .models import *

class ConatctForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': "Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': "Email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder': "Message"
    }))
    class Meta:
        model = ContactUs
        fields = '__all__'


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
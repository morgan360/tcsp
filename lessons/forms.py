from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['start_time']
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
        }

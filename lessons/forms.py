from django import forms
from .models import PublicClasses


class ProductForm(forms.ModelForm):
    class Meta:
        model = PublicClasses
        fields = ['start_time']
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
        }

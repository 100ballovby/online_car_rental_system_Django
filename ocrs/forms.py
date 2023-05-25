from django import forms
from .models import Car, Order, FeedbackMsg
from tinymce.widgets import TinyMCE


class CarForm(forms.ModelForm):
    class Meta:
        model = Car   # модель, на основе которой строится форма
        fields = [
            "image",
            "company_name",
            "num_of_seats",
            "cost_per_day",
            "content",
        ]  # поля для формы
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'company_name': forms.Select(attrs={'class': 'form-select form-control'}),
            'num_of_seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_per_day': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': TinyMCE(attrs={'cols': 100, 'rows': 20})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'address',
            'start_date',
            'end_date',
        ]
        widgets ={
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMsg
        exclude = ("checked",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'contact': TinyMCE(attrs={'cols': 100, 'rows': 20})
        }

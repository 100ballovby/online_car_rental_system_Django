from django import forms
from .models import Car, Order, FeedbackMsg
from tinymce.widgets import TinyMCE


class CarForm(forms.ModelForm):
    class Meta:
        model = Car   # модель, на основе которой строится форма
        fields = [
            "image",
            "car_name",
            "company_name",
            "num_of_seats",
            "cost_per_day",
            "content",
        ]  # поля для формы


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'car_name',
            'employee_name',
            'cell_no',
            'address',
            'start_date',
            'end_date',
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMsg
        exclude = ("checked",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'contact': TinyMCE(attrs={'cols': 100, 'rows': 20})
        }

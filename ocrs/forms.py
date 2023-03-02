from django import forms
from .models import Car, Order, FeedbackMsg


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
        fields = '__all__'

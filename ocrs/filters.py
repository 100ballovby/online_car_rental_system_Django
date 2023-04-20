import django_filters as df
from .models import Car
from django import forms


class CarFilter(df.FilterSet):
    class Meta:
        model = Car
        fields = ('car_name', 'company_name',)
        widgets = {
            'company_name': forms.Select(
                attrs={'class': 'selectpicker'}
            )
        }



from django.contrib import admin
from .models import Car, Order, Brands, Specifications
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "cost_per_day", "image", "booked",)
    list_editable = ("cost_per_day",)
    list_filter = ("cost_per_day", "booked",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("car_name", "start_date", "end_date", "closed", "employee_name",)
    list_editable = ("end_date", "closed",)
    list_filter = ("employee_name", "closed", "car_name",)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "segment",)
    list_filter = ("segment",)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ("name",)



admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brands, BrandAdmin)
admin.site.register(Specifications, SpecificationsAdmin)

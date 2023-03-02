from django.db import models
from django.utils.safestring import mark_safe
from tinymce import models as tinymce_models
from django import forms

# Create your models here.


def uploaded_location(inst, f_name):
    return f"{inst.car_name}/{f_name}"


class Brands(models.Model):
    BRAND_CHOICES = (
        ("B", "Стандарт"),
        ("C", "Стандарт+"),
        ("E", "Бизнес"),
        ("F", "Премиум"),
    )

    brand_name = models.CharField(max_length=100)
    wiki_link = models.URLField()
    segment = models.CharField(max_length=100, choices=BRAND_CHOICES)

    class Meta:
        ordering = ["segment",]
        verbose_name = "Автомобильный бренд"  # название на странице добавления сущности в БД
        verbose_name_plural = "Автомобильные бренды"  # название в админке

    def __str__(self):
        return self.brand_name



class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    car_name = models.CharField(max_length=100)
    company_name = models.ForeignKey(Brands, on_delete=models.CASCADE, default=None)
    # организуем связь между полем company_name и таблицей Brands
    num_of_seats = models.IntegerField()
    cost_per_day = models.CharField(max_length=50)
    content = tinymce_models.HTMLField(max_length=7000, blank=True, null=True, db_index=True)
    like = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Машину"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return f'/car/{self.id}'


class Order(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=20)
    address = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.car_name.car_name

    def get_absolute_url(self):
        return f'/car/detail/{self.id}'


class FeedbackMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = tinymce_models.HTMLField(max_length=7000, blank=True, null=True, db_index=True)


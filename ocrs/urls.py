from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('carlist/', views.car_list, name="car_list"),
    path('create_order/', views.create_order, name="create_order"),
    path('detail/<int:order_id>/', views.order_detail, name="order_detail"),
    path('delete_order/<int:order_id>/', views.order_delete, name="order_delete"),
    path('detail/<str:name>/', views.car_detail, name="car_detail"),
    path('edit/<int:car_id>/', views.car_edit, name="car_edit"),
    path('delete_car/<int:car_id>/', views.car_delete, name="car_delete"),
    path('newcar/', views.new_car, name="new_car"),
    path('contacts/', views.contacts, name="contacts"),
    path('popular_cars/', views.popular_cars, name="popular_cars"),
    path('like/<int:car_id>/', views.like_update, name="like")
]
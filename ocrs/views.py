from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q  # работа с поисковыми запросами в Django
from .models import Car, Order, FeedbackMsg
from .filters import CarFilter
from .forms import CarForm, OrderForm, FeedbackForm
from promo.models import PromoBlock
from datetime import datetime
# Create your views here.


def home(request):
    now = datetime.now()
    slider_data = PromoBlock.objects.filter(active_from__lte=now,
                                            active_to__gte=now).order_by('position')
    return render(request, "home.html", {'title': "Car rental | Minsk",
                                         'slider': slider_data})


def car_list(request):
    cars = Car.objects.all()

    cars_filter = CarFilter(request.GET, queryset=cars)  # фильтровать список cars формой с методом get
    cars = cars_filter.qs

    query = request.GET.get('q')  # забираем запрос от формы с методом отправки GET
    if query:  # если запрос состоялся
        cars = cars.filter(
            Q(car_name__icontains=query),
            Q(company_name__icontains=query),
            Q(cost_per_day__icontains=query),
            Q(num_of_seats__icontains=query)
        )
    # пагинация
    paginator = Paginator(cars, 5)  # отображаем по 5 машин на странице
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:  # если пользователь вписал номер страницы как текст
        cars = paginator.page(1)  # перенесем его на первую страницу с машинами
    except EmptyPage:  # если пользователь вписал номер страницы, например, 9999999
        cars = paginator.page(paginator.num_pages)  # перемещаем его на последнюю страницу с машинами
    return render(request, "car_list.html", {'cars': cars, 'filter': cars_filter})


def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "create_order.html", {"title": "Create order",
                                                 "form": form})


def order_detail(request, order_id=None):
    detail = get_object_or_404(Order, order_id=order_id)
    return render(request, "order_detail.html", {"detail": detail})


def order_update(request, order_id=None):
    detail = get_object_or_404(Order, order_id=order_id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "order_update.html", {"form": form,
                                                 "title": "Update order info"})


def order_delete(request, order_id=None):
    query = get_object_or_404(Order, order_id=order_id)
    query.delete()
    return redirect('home')


def car_detail(request, brand, car_id=None):
    detail = get_object_or_404(Car, car_id=car_id)
    return render(request, "car_detail.html", {"detail": detail})


def car_edit(request, car_id=None):
    query = get_object_or_404(Car, car_id=car_id)
    form = CarForm(request.POST or None, instance=query)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "car_edit.html", {"form": form, "title": "Update car info"})


def car_delete(request, car_id=None):
    query = get_object_or_404(Car, car_id=car_id)
    query.delete()
    cars = Car.objects.all()
    return render(request, "admin_index.html", {"cars": cars})


def new_car(request):
    new = Car.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(car_name__icontains=query),
            Q(company_name__icontains=query),
            Q(cost_per_day__icontains=query),
            Q(num_of_seats__icontains=query)
        )
    paginator = Paginator(new, 12)
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        new = paginator.page(1)
    except EmptyPage:
        new = paginator.page(paginator.num_pages)
    return render(request, "new_car.html", {"car": new})


def contacts(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('contacts')
    return render(request, "contacts.html",  {"title": "Contact with us",
                                              "form": form})


def like_update(request, car_id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, car_id=car_id)
    like_count.like += 1
    like_count.save()
    return render(request, "new_car.html", {"car": new})


def popular_cars(request):
    popular = Car.objects.order_by('-like')
    return render(request, "popular_cars.html", {"popular": popular})

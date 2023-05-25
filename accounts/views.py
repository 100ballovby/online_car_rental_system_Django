from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm
# Create your views here.


def logout_view(request):
    logout(request)
    #return render(request, "home.html")
    return redirect("home")


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)  # сохраняем пользователя, но НЕ добавляем в БД
        password = form.cleaned_data.get("password")  # забираем пароль
        user.set_password(password)  # устанавливаем хэш для пароля
        user.save()  # добавляем пользователя в БД

        return redirect("/login/")
    return render(request, "form.html", {"form": form,
                                         "title": "Register"})

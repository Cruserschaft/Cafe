from django.shortcuts import render
from django.http import HttpResponse
from .models import DishType, Menu, Gallery
from .forms import UserReservationForm
import random
import re


def validation(regular, value):
    print(regular)
    print(value)
    print(re.findall(regular, value))
    return len(re.findall(regular, value)) == 1


def start(request):
    if request.method == "POST":
        name_valid = r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}"
        email_valid = r"[A-Za-z.-]{3,10}@[A-Za-z0-9]{4,}.[a-z]{3,3}"
        phone_valid = r"(\+380?|380?|0)[0-9]{9}"
        date_valid = r"[0-9]{2}.[0-9]{2}.[0-9]{2,4}"
        time_valid = r"[0-9]{2}[.,:][0-9]{2}$"
        of_people_valid = r"[0-9]{1,2}"

        if not validation(name_valid, request.POST["name"]):
            return HttpResponse("Name")
        if not validation(email_valid, request.POST["email"]):
            return HttpResponse("email")
        if not validation(phone_valid, request.POST["phone"]):
            return HttpResponse("phone")
        if not validation(date_valid, request.POST["date_order"]):
            return HttpResponse("date_order")
        if not validation(time_valid, request.POST["time_order"]):
            return HttpResponse(request.POST["time_order"])
        if not validation(of_people_valid, request.POST["of_people"]):
            return HttpResponse("of_people")

        return HttpResponse("Alls great")

    categories = DishType.objects.filter(dish_type_access=True)
    dishes = Menu.objects.filter(dish_is_special=False, dish_access=True)
    dishes_specials = Menu.objects.filter(dish_is_special=True, dish_access=True)
    gallery = Gallery.objects.filter(visible=True)
    gallery = random.choices(gallery, k=4)
    user_reservation = UserReservationForm()

    return render(request, "main.html", context={
        "category": categories,
        "dishes": dishes,
        "special_dishes": dishes_specials,
        "gallery": gallery,
        "reservation_form": user_reservation,
    })

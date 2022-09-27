from django.shortcuts import render
from django.http import HttpResponse
from .models import DishType, Menu, Gallery
from .forms import UserReservationForm
import random
import re


class Wrong:
    wrong = False


def validation(regular, value):
    print(regular)
    print(value)
    print(re.findall(regular, value))
    return len(re.findall(regular, value)) == 1


def start(request):
    global wrong
    categories = DishType.objects.filter(dish_type_access=True)
    dishes = Menu.objects.filter(dish_is_special=False, dish_access=True)
    dishes_specials = Menu.objects.filter(dish_is_special=True, dish_access=True)
    gallery = Gallery.objects.filter(visible=True)
    gallery = random.choices(gallery, k=4)
    user_reservation = UserReservationForm()

    if request.method == "POST":
        name_valid = r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}"
        email_valid = r"[A-Za-z.-]{3,10}@[A-Za-z0-9]{4,}.[a-z]{3,3}"
        phone_valid = r"(\+380?|380?|0)[0-9]{9}"
        date_valid = r"[0-9]{2}.[0-9]{2}.[0-9]{2,4}"
        time_valid = r"[0-9]{2}[.,:][0-9]{2}$"
        of_people_valid = r"[0-9]{1,2}"

        wrong = Wrong()

        if not validation(name_valid, request.POST["name"]):
            wrong.name = "Невірно набране ім'я"
            wrong.wrong = True
        if not validation(email_valid, request.POST["email"]):
            wrong.email = "Невірний емейл"
            wrong.wrong = True
        if not validation(phone_valid, request.POST["phone"]):
            wrong.phone = "Невірний телефон"
            wrong.wrong = True
        if not validation(date_valid, request.POST["date_order"]):
            wrong.date_order = "Невірна дата"
            wrong.wrong = True
        if not validation(time_valid, request.POST["time_order"]):
            wrong.time_order = "Невірний час"
            wrong.wrong = True
        if not validation(of_people_valid, request.POST["of_people"]):
            wrong.of_people = "Невірна кількість місць"
            wrong.wrong = True

        if wrong.wrong:
            user_reservation = UserReservationForm(request.POST)
        else:
            pass
            # UserReservationForm(request.POST).save()

    return render(request, "main.html", context={
        "category": categories,
        "dishes": dishes,
        "special_dishes": dishes_specials,
        "gallery": gallery,
        "reservation_form": user_reservation,
        "wrong": wrong,

    })

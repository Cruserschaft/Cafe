from django.shortcuts import render
from django.http import HttpResponse
from .models import DishType, Menu, Gallery
from .forms import UserReservationForm
import random


def start(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        date_order = request.POST["date_order"]
        time_order = request.POST["time_order"]
        of_people = request.POST["of_people"]
        message = request.POST["message"]
        return HttpResponse(f"{name}, {email}, {phone}, {date_order}, {time_order}, {of_people}, {message};")

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




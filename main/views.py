from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import UserReservationForm
import random
import re


def start(request):
    categories = DishType.objects.filter(dish_type_access=True)
    dishes = Menu.objects.filter(dish_is_special=False, dish_access=True)
    dishes_specials = Menu.objects.filter(dish_is_special=True, dish_access=True)
    gallery = Gallery.objects.filter(visible=True)
    gallery = random.choices(gallery, k=4)
    carousel = Carousel.objects.filter(carousel_access=True)
    about = About.objects.all()[0]
    whuus = Whuus.objects.all().order_by("whuus_order")
    chefs = Chefs.objects.all().order_by("chefs_order")
    events = Events.objects.all().order_by("event_order")
    contacts = Contacts.objects.all()[0]
    testers = Testimonials.objects.all().order_by("test_order")
    user_reservation = UserReservationForm()
    err = None

    if request.method == "POST":
        user_reservation = UserReservationForm(request.POST)
        err = user_reservation.errors.as_data()

        if user_reservation.is_valid():
            form_update = user_reservation.save(commit=True)
            form_update.save()
            return redirect("/")

    return render(request, "main.html", context={
        "carousel": carousel,
        "about": about,
        "whuus": whuus,
        "category": categories,
        "dishes": dishes,
        "events": events,
        "special_dishes": dishes_specials,
        "chefs": chefs,
        "gallery": gallery,
        "testers": testers,
        "contacts": contacts,
        "reservation_form": user_reservation,
        "error": err,
    })

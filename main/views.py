from django.shortcuts import render
from django.http import HttpResponse
from .models import DishType, Menu


def start(request):
    categories = DishType.objects.filter(dish_type_access=True)
    dishes = Menu.objects.filter(dish_is_special=False, dish_access=True)
    dishes_specials = Menu.objects.filter(dish_is_special=True, dish_access=True)

    return render(request, "main.html", context={
        "category": categories,
        "dishes": dishes,
        "special_dishes": dishes_specials,
    })
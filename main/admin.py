from django.contrib import admin
from .models import DishType, Menu, Gallery
from manager.models import UserReservations

# Register your models here.

admin.site.register(DishType)
admin.site.register(Menu)
admin.site.register(Gallery)
admin.site.register(UserReservations)


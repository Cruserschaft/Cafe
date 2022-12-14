from django.contrib import admin
from .models import *


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ("dish_type", "dish_order", "dish_name", "dish_cost", "dish_access", "dish_is_special")
    list_display_links = ("dish_order", "dish_name", "dish_cost", "dish_access", "dish_is_special")
    # list_editable - to instant change in admin panel


class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("dish_type_name", "dish_type_order", "dish_type_access")
    list_display_links = ("dish_type_name", "dish_type_order", "dish_type_access")


admin.site.register(DishType, DishTypeAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Gallery)
admin.site.register(Carousel)
admin.site.register(About)
admin.site.register(Whuus)
admin.site.register(Chefs)
admin.site.register(Events)
admin.site.register(Testimonials)
admin.site.register(Contacts)


import os.path

from django.db import models
import uuid


class DishType(models.Model):
    dish_type_name = models.CharField(max_length=50, unique=True)
    dish_type_order = models.PositiveIntegerField(unique=True)
    dish_type_access = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.dish_type_name}: {self.dish_type_order}"

    class Meta:
        verbose_name = "Категорії"
        ordering = ("dish_type_order", )


class Menu(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/dishes/', filename)

    dish_name = models.CharField(max_length=50, unique=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    dish_cost = models.DecimalField(max_digits=8, decimal_places=2)
    dish_ingredients = models.CharField(max_length=300)
    dish_access = models.BooleanField(default=True)
    dish_order = models.SmallIntegerField()
    dish_is_special = models.BooleanField(default=False)
    dish_image = models.ImageField(upload_to=get_file_name)
    dish_about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.dish_type.dish_type_name}: {self.dish_order}: {self.dish_name}: "

    class Meta:
        verbose_name = "Страви"
        ordering = ("dish_type", )


class Events(models.Model):
    event_title = models.TextField()
    event_cost = models.PositiveIntegerField()
    event_about_start = models.TextField()
    event_about1 = models.TextField(blank=True)
    event_about2 = models.TextField(blank=True)
    event_about3 = models.TextField(blank=True)
    event_about_finish = models.TextField(blank=True)


class About(models.Model):
    about_title = models.TextField()
    about_start_text = models.TextField()
    about_p1 = models.TextField()
    about_p2 = models.TextField(blank=True)
    about_p3 = models.TextField(blank=True)
    about_end = models.TextField(blank=True)



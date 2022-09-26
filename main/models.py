import os.path

from django.db import models
import uuid


class DishType(models.Model):
    dish_type_name = models.CharField(max_length=50, unique=True, verbose_name="Назва категорії")
    dish_type_order = models.PositiveIntegerField(unique=True, verbose_name="Порядок")
    dish_type_access = models.BooleanField(default=True, verbose_name="Доступ")

    def __str__(self):
        return f"{self.dish_type_name}"

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ("dish_type_order", )


class Menu(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/dishes/', filename)

    dish_name = models.CharField(max_length=50, unique=True, verbose_name="Назва стави")
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, verbose_name="Тип страви")
    dish_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Вартість")
    dish_ingredients = models.CharField(max_length=300)
    dish_access = models.BooleanField(default=True, verbose_name="Доступ")
    dish_order = models.SmallIntegerField(verbose_name="Порядок")
    dish_is_special = models.BooleanField(default=False, verbose_name="Спеціальна")
    dish_image = models.ImageField(upload_to=get_file_name)
    dish_about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.dish_type.dish_type_name}: {self.dish_order}: {self.dish_name}"

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"
        ordering = ("dish_type", "dish_order")


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


class Gallery(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        ordering = ("photo", )

    def __str__(self):
        return self.photo.__str__()


